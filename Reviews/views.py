from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View

# Create your views here.

# class view
class ReviewView(View):
    # called when there is a get request
    def get(self,request):
        form = ReviewForm()            # create a new form instance
        return render(request,'Reviews/review.html',{'form':form})     # render the form

    
    # automatically called when there is a post request
    def post(self,request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()                # save the data to the database
            return HttpResponseRedirect("/thank-you")

        # if form is not valid render the page with same form instance
        return render(request,'Reviews/review.html',{'form':form})        

'''
def review(request):
    # there are two different request coming to this view so check for POST as POST have the data
    if request.method == "POST":      
        form = ReviewForm(request.POST)                 # getting form data from POST method
        
        # if the form is valid render thank-you page
        # django automatically check the form for it's validness
        # nothing needs to change here this is_valid function works for all the field which added right now 
        # that's the beauty of using django forms also fields data is also saved in cleaned_data dictionary
        if form.is_valid():
            # if we are using ModelForm then there is no need to create a Model instance pass the value
            # we can directly call save on form
            form.save()                # save the data to the database
            return HttpResponseRedirect("/thank-you")        # / denote the host url, good practise to redirect rather then directly render thank-you page here

    else: 
        form = ReviewForm()          # initiate the form
    
    # if the is_valid returns false, then it will send the pre entered form with pre-entered values and also the errors
    # it show an error when the field is empty to check the error open elements from inspect and remove required from user_name field
    return render(request,'Reviews/review.html',{'form':form})            
'''

def thank_you(request):
    return render(request,"Reviews/thank-you.html")




