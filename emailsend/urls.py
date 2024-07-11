from django.urls import path
from . import views

urlpatterns = [
  path('', views.ContactFormAPi.as_view(), name='Send Emial Message')
]
