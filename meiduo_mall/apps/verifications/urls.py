

from apps.verifications.views import ImageCodeView
from django.urls import path

urlpatterns = [
    path('image/<uuid>/count/', ImageCodeView.as_view()),
    
    
]