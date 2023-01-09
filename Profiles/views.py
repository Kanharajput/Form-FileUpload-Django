from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .models import UserProfile
from django.views.generic.edit import CreateView


# Create your views here.
# this will create the form according to model columns and also save data automatically
# as every field is related with every column so the data which is entered in a field is 
# directly saved to column thorough which it is created
# by default it send the form dictionary to the template
class CreateProfileView(CreateView):
    model = UserProfile
    fields = "__all__"
    template_name = "Profiles/create_profile.html"
    success_url = "/thank-you"
    