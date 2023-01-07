from django.urls import path
from . import views

urlpatterns = [
    path("",views.review),                  # url http://127.0.0.1:8000/
    path("thank-you",views.thank_you),         # url http://127.0.0.1:8000/thank-you
]
