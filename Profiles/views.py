from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect


def storeFile(file):                                      # naive approach to save the file
    # right now it only work for jpg files
    # create a temp folder in root directory it will automatically create image.jpg in that folder and write the data
    with open("temp/image.jpg", "wb+") as dest:           # open a destination manually where we can write the file
        for chunk in file.chunks():                       # make chuck of the file means small part
            dest.write(chunk)                             # write a chunk each time

# Create your views here.
class CreateProfileView(View):
    def get(self,request):
        return render(request,"Profiles/create_profile.html")

    def post(self,request):
        storeFile(request.FILES["image_name"])        # file is the dictionary provided by django to access files
        return HttpResponseRedirect("/thank-you")