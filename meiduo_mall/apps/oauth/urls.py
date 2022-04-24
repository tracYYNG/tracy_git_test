from django.urls import path
from apps.oauth.views import QQLoginURLView,OAuthQQView


urlpatterns = [
    path('oauth/qq/authorization/', QQLoginURLView.as_view()),
    path('oauth/qq/user/',OAuthQQView.as_view())
]