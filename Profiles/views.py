from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfileForm
from .models import UserProfile


# Create your views here.
class CreateProfileView(View):
    def get(self,request):
        form = ProfileForm()       
        return render(request,"Profiles/create_profile.html",{"form":form})

    def post(self,request):
        # valid the form , right now we have only files but if we have files and other data then this is how 
        # we pass it to Form class for validation 
        form = ProfileForm(request.POST,request.FILES)

        # if form is valid save the data
        if form.is_valid():    
            image = UserProfile(image=request.FILES["user_image"])
            image.save()
            return HttpResponseRedirect("/thank-you")

        return render(request,"Profiles/create_profile.html",{"form":form})