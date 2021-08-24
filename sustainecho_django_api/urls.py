from django.urls import path
from .views import CityGenericAPIView

urlpatterns = [
    path('city/', CityGenericAPIView.as_view())
]
