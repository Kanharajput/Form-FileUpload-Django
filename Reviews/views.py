from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def review(request):
    # there are two different request coming to this view so check for POST as POST have the data
    if request.method == "POST":             
        entered_name = request.POST['username']         # request have POST as dictionary and name which is html as key entered data by user is the value

        if entered_name == "":
            return render(request,'Reviews/review.html',{'has_error':True})

        print(entered_name)
        return HttpResponseRedirect("/thank-you")        # / denote the host url, good practise to redirect rather then directly render thank-you page here

    return render(request,'Reviews/review.html',{'has_error':False})            # for GET request this review.html is render


def thank_you(request):
    return render(request,"Reviews/thank-you.html")




