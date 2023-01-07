from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm


# Create your views here.

def review(request):
    # there are two different request coming to this view so check for POST as POST have the data
    if request.method == "POST":      
        form = ReviewForm(request.POST)                 # getting form data from POST method
        
        # if the form is valid render thank-you page
        # django automatically check the form for it's validness
        if form.is_valid():
            print(form.cleaned_data)       # cleaned_data is a dictionary having user entered data in key-value pair
            return HttpResponseRedirect("/thank-you")        # / denote the host url, good practise to redirect rather then directly render thank-you page here

    # below code is for GET request
    form = ReviewForm()          # initiate the form
    return render(request,'Reviews/review.html',{'form':form})            # for GET request this review.html is render


def thank_you(request):
    return render(request,"Reviews/thank-you.html")




