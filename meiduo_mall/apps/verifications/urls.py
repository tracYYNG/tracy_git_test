

from apps.verifications.views import ImageCodeView,SmsCodeView
from django.urls import path, register_converter

from utils.converter import MobileConverter

register_converter(MobileConverter,'mobile')

urlpatterns = [
    path('image/<uuid>/count/', ImageCodeView.as_view()),
    path('sms/<mobile:mobile>/', SmsCodeView.as_view()),
    
    
]

