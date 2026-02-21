from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import DocumentRequest, File, Signature

class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'client/index.html')
    

class NotificationsView(LoginRequiredMixin, View):
    def get(self, request):
        request_docs = DocumentRequest.objects.filter(user=request.user).order_by("-request_id")
        return render(request, 'client/notifications.html',{"requests":request_docs})
    

class SettingsView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'client/settings.html')
    

class DocumentView(LoginRequiredMixin, View):
    def get(self, request, id):
        doc = DocumentRequest.objects.get(user=request.user,request_id=id)
        files = File.objects.filter(document_request=doc)
        try:
            singature = Signature.objects.get(document=doc)
        except Signature.DoesNotExist:
            singature = "null"
        return render(request, 'client/viewer.html',{"doc":doc,"files":files,"signature":singature})


class DocumentsView(LoginRequiredMixin, View):
    def get(self,request,d_type):
        if d_type == 'all':
            docs = DocumentRequest.objects.filter(user=request.user).order_by("-request_id")
        elif d_type == 'signed':
            docs = DocumentRequest.objects.filter(user=request.user,status='signed').order_by("-request_id")
        elif d_type == 'rejected':
            docs = DocumentRequest.objects.filter(user=request.user,status='rejected').order_by("-request_id")
        elif d_type == 'pending':
            docs = DocumentRequest.objects.filter(user=request.user,status='pending').order_by("-request_id")
        return render(request,'client/documents.html',{"docs":docs})