
from django.urls import path, register_converter
from apps.user.views import MobileCountView, RegisterView, UsernameCountView,LoginView

from utils.converter import UserConverter,MobileConverter

# class UserConverter:
#     regex = "[0-9A-Za-z]{5,20}"

#     def to_python(self, value):
#         return value

# class MobileConverter:
#     regex = "(13[0-9]|14[01456879]|15[0-35-9]|16[2567]|17[0-8]|18[0-9]|19[0-35-9])\d{8}"

#     def to_python(self, value):
#         return value

register_converter(UserConverter,'user')
register_converter(MobileConverter,'mobile')

urlpatterns = [
    path('username/<user:username>/count/', UsernameCountView.as_view()),
    path('mobiles/<mobile:mobiles>/count/',MobileCountView.as_view()),
    path('user/',RegisterView.as_view()),
    path('authorizations/',LoginView.as_view()),
]