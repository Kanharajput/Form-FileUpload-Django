from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect


# Create your views here.

class CreateProfileView(View):
    def get(self,request):
        return render(request,"Profiles/create_profile.html")

    def post(self,request):
        print(request.FILES["image_name"])        # file is the dictionary provided by django to access files
        return HttpResponseRedirect("/thank-you")