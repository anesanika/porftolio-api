from rest_framework import viewsets
from .serializer import ProjectSerializer
from .models import Project

# Create your views here.

class ProjectViews(viewsets.ReadOnlyModelViewSet):
  queryset = Project.objects.all()
  serializer_class = ProjectSerializer
  