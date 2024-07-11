from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static


route = DefaultRouter()
route.register(r"", views.ProjectViews, basename="myProjects")

urlpatterns = [
  path('projects/', include(route.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
