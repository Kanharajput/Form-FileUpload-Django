from django.urls import path
from . import views

urlpatterns = [
    #path("",views.review),                  # url http://127.0.0.1:8000/
    # path for class view
    path("",views.ReviewView.as_view()),          # url http://127.0.0.1:8000/
    path("thank-you",views.ThankYouView.as_view()),         # url http://127.0.0.1:8000/thank-you
    path("reviews",views.AllReviewClass.as_view()),
    path("reviews/favourite",views.SaveFavourite.as_view()),      # write it above slug path otherwise slug path will accept the url
    path("reviews/<pk>",views.DetailedReviewClass.as_view(),name="detail-indent"),
]
