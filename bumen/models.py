from django.db import models
from users.models import User, Company
import uuid

status_t = [
    ('signed','signed'),
    ('pending','pending'),
    ('rejected','rejected')
]

notification_t = [
    ('standard','standard'),
    ('warning','warning'),
    ('alert','alert')
]

class DocumentRequest(models.Model):
    request_id = models.UUIDField(primary_key=True,default=uuid.uuid4,unique=True,editable=False)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL,null=True,blank=True)
    status = models.CharField(choices=status_t,default='pending',max_length=20)
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True,related_name='request_documents')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.company.name} - {self.request_id}'

class Signature(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True,related_name='signs',editable=False)
    document = models.OneToOneField(DocumentRequest, on_delete=models.SET_NULL, null=True,blank=True,related_name='signs',editable=False)
    sign = models.UUIDField(primary_key=True,default=uuid.uuid4,unique=True,editable=False)
    created_at = models.DateField(auto_now_add=True,editable=False)
    created_at_detailed = models.DateTimeField(auto_now_add=True,editable=False)

class VerificationRequest(models.Model):
    request_id = models.UUIDField(primary_key=True,default=uuid.uuid4,unique=True,editable=False)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL,null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True,related_name='verification_requests')
    created_at = models.DateField(auto_now_add=True)

class Action(models.Model):
    action_id = models.UUIDField(primary_key=True,default=uuid.uuid4,unique=True,editable=False)
    desc = models.CharField(max_length=150,default="")
    status = models.CharField(choices=status_t,default='standard',max_length=20)
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True)
    created_at = models.DateField(auto_now_add=True)

class File(models.Model):
    file_id = models.UUIDField(primary_key=True,default=uuid.uuid4,unique=True,editable=False)
    file = models.FileField(upload_to='documents/')
    document_request = models.ForeignKey(DocumentRequest, on_delete=models.SET_NULL, null=True,blank=True,related_name='files')
    company = models.ForeignKey(Company, on_delete=models.SET_NULL,null=True,blank=True,related_name='files')
    created_at = models.DateField(auto_now_add=True)