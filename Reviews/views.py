from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def review(request):
    return HttpResponse("Revies app succesfully linked with project")