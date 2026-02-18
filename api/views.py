from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from bumen.models import DocumentRequest, Action, File, Signature

class DocumentRejectAPI(APIView):
    def post(self,request):
        doc_id = request.data.get("uuid")
        doc = DocumentRequest.objects.get(request_id=doc_id)
        doc.status = 'rejected'
        doc.save()
        Action(
            desc="Document signed",
            status="standard",
            user=request.user
        ).save()
        return Response({"status":True,"msg":"Success"})

class DocumentSignAPI(APIView):
    def post(self,request):
        doc_id = request.data.get("uuid")
        doc = DocumentRequest.objects.get(request_id=doc_id)
        doc.status = 'signed'
        doc.save()
        sign = Signature(
            user=request.user,
            document=doc
        )
        sign.save()
        Action(
            desc="Document rejected",
            status="standard",
            user=request.user
        ).save()
        return Response({"status":True,"msg":"Success","signature":str(sign.sign)})