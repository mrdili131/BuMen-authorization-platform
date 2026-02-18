from django.contrib import admin
from .models import DocumentRequest, VerificationRequest, Action, File, Signature

admin.site.register([DocumentRequest, VerificationRequest, Action, File, Signature])