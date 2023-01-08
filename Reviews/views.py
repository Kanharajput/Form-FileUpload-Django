from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic import TemplateView

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


# TemplateView is a special class for handling templates in class
class ThankYouView(TemplateView):
    template_name = "Reviews/thank-you.html"           # this will render the thank-you page
    
    # if we want to some data like dictinary then we have to use predefined function
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "Successfully pass the data"
        return context


# render review page which have username and rating of all reviews
class AllReviewClass(TemplateView):
    template_name = "Reviews/all_review.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.all()
        context["reviews"] = reviews
        return context