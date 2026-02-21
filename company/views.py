from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .utils import is_company
from .forms import DocumentUploadForm
from bumen.models import DocumentRequest, File
from users.models import User

class IndexView(LoginRequiredMixin,View):
    def get(self,request):
        if is_company(request):
            return render(request,'company/index.html')
        return redirect('home')
    
class CreateRequest(LoginRequiredMixin,View):
    def get(self,request):
        if is_company(request):
            form = DocumentUploadForm()
            return render(request,'company/create_request.html',{"form":form})
        return redirect('home')
    
    def post(self,request):
        if is_company(request):
            form = DocumentUploadForm(request.POST,request.FILES)
            if form.is_valid():
                files = request.FILES.getlist("files")
                try:
                    client = User.objects.get(pinfl=form.cleaned_data["pinfl"])
                except User.DoesNotExist:
                    return render(request,'company/create_request.html',{"form":form,"msg":"Mijoz topilmadi"})
                doc = DocumentRequest(
                    start_date = form.cleaned_data["start_date"],
                    end_date = form.cleaned_data["end_date"],
                    company = request.user.company,
                    desc = form.cleaned_data["desc"],
                    user = client
                )
                doc.save()
                for i in files:
                    File.objects.create(
                        file = i,
                        document_request = doc,
                        company = request.user.company
                    ).save()
                return render(request,'company/create_request.html',{"form":form})
        return render(request,'company/create_request.html',{"form":form})
