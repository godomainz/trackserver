from django.urls import path, include
from rest_framework.routers import DefaultRouter
from track import views

router = DefaultRouter()
router.register('track', views.TrackViewSet)
app_name = 'track'

urlpatterns = [
    path('', include(router.urls))
]