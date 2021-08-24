from django.shortcuts import render

# Create your views here.
def accept(req):
    return render(req,"accept.html")