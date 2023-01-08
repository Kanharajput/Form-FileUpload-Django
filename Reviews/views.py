from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from django.views.generic import ListView,DetailView

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


# ListView to render the list of items/data
class AllReviewClass(ListView):
    template_name = "Reviews/all_review.html"
    model = Review                               # all the entries are now sent to template 
    context_object_name = "reviews"               # change the by default object_list to reviews

    def get_queryset(self):
        # this is the base query through which we generate our needed query
        base_query = super().get_queryset()         # django hit the database at last when a single query is generated 
        entries_rating_gt3 = base_query.filter(rating__gt=3)     # only those entries whose rating is greater 3
        return entries_rating_gt3


# it match slug with models field and return a matched entry
# make sure slug name should be pk, so it is identified by DetailView
# DetailView only useful when there is only one comparison and they may be a primary key
class DetailedReviewClass(DetailView):
    template_name = "Reviews/detail_review.html"
    model = Review                      

