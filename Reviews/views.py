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
        # nothing needs to change here this is_valid function works for all the field which added right now 
        # that's the beauty of using django forms also fields data is also saved in cleaned_data dictionary
        if form.is_valid():
            print(form.cleaned_data)       # cleaned_data is a dictionary having user entered data in key-value pair
            return HttpResponseRedirect("/thank-you")        # / denote the host url, good practise to redirect rather then directly render thank-you page here

    else:
        # if the request is GET then create a new form
        form = ReviewForm()          # initiate the form
    
    # if the is_valid returns false, then it will send the pre entered form with pre-entered values and also the errors
    # it show an error when the field is empty to check the error open elements from inspect and remove required from user_name field
    return render(request,'Reviews/review.html',{'form':form})            


def thank_you(request):
    return render(request,"Reviews/thank-you.html")




