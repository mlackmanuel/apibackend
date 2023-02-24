from django.urls import path

from rest_framework import routers
from .views import ContactAPIView 

router=routers.DefaultRouter()
urlpatterns=router.urls
urlpatterns = [
    path('contact/',ContactAPIView.as_view(),name='contact-list')
]
