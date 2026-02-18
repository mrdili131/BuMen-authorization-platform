from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import DocumentRequest, File

class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'index.html')
    

class NotificationsView(LoginRequiredMixin, View):
    def get(self, request):
        request_docs = DocumentRequest.objects.filter(user=request.user).order_by("-created_at")
        return render(request, 'notifications.html',{"requests":request_docs})
    

class SettingsView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'settings.html')
    

class DocumentView(LoginRequiredMixin, View):
    def get(self, request, id):
        doc = DocumentRequest.objects.get(user=request.user,request_id=id)
        files = File.objects.filter(document_request=doc)
        return render(request, 'viewer.html',{"doc":doc,"files":files})