from django.urls import path
from . import views

urlpatterns = [
    #path("",views.review),                  # url http://127.0.0.1:8000/
    # path for class view
    path("",views.ReviewView.as_view()),          # url http://127.0.0.1:8000/
    path("thank-you",views.ThankYouView.as_view()),         # url http://127.0.0.1:8000/thank-you
]
