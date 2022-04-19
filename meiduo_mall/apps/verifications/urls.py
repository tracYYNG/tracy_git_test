

from apps.verifications.views import ImageCodeView
from django.urls import path

urlpatterns = [
    path('image/<uuid>/count/', ImageCodeView.as_view()),
    
    
]

# http://demo.open.renren.io/renren-fast-server/captcha.jpg?uuid=a11212f8-e1e4-4eb8-8cb6-51731b03e953