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

def thank_you(request):
    return render(request,"Reviews/thank-you.html")




