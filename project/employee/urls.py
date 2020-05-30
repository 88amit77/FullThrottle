from django.urls import path, include

from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'members', views.MembersViewSet, basename='members')
router.register(r'punch_time', views.InOutViewSet, basename='punch_time')
router.register(r'report', views.ReportViewSet, basename='report')


urlpatterns = [
               path('', include(router.urls)),
              ]