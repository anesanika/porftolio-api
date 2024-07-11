from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import EmailMessage
from rest_framework.permissions import AllowAny
from django.conf import settings

# Create your views here.

class ContactFormAPi(APIView):
  permission_classes = [AllowAny]
  def post(self, request):
    
    recipient_email = 'anesaininika@gmail.com'
    subject = request.data['subject']
    body = request.data['body']

    emailw = EmailMessage(subject, body , settings.EMAIL_HOST_USER, [recipient_email])
    emailw.send(fail_silently=False)
    return Response({'status': True, 'message': 'Email sent successfully'})