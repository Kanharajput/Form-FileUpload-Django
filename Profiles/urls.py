from django.urls import path
from . import views

urlpatterns = [
    path("",views.CreateProfileView.as_view()),
    path("all-profiles",views.AllProfiles.as_view()),
]
