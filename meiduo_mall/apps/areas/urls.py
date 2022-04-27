from django.urls import path
from apps.areas.views import AddressView,CityView


urlpatterns = [
    path('areas/', AddressView.as_view()),
    path('areas/<hlevel_id>/',CityView.as_view())
]