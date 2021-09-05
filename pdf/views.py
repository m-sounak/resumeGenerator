from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, render
from .models import Profile
from django.urls import reverse
from django.template import loader
import pdfkit
import io


# Create your views here.
def accept(req):
    if req.method == "POST":
        name = req.POST.get("name","")
        phone = req.POST.get("phone","")
        linkedin = req.POST.get("linkedin","")
        email = req.POST.get("email","")
        github = req.POST.get("github","")
        
        school = req.POST.get("school","")
        degree = req.POST.get("degree","")
        passyear = req.POST.get("passyear","")
        cgpa = req.POST.get("cgpa","")
        
        post = req.POST.get("post","")
        company = req.POST.get("company","")
        
        skills = req.POST.get("skills","")
        
        achievements = req.POST.get("achievements","")
        
        extracurr = req.POST.get("extracurr","")

        profile = Profile(name = name, phone = phone, linkedin = linkedin, email = email, github = github, 
            school = school, degree = degree, passyear = passyear, cgpa = cgpa,
            post = post, company = company, skills = skills, achievements = achievements, extracurr = extracurr)
        profile.save()
        #return HttpResponseRedirect('accept')
        return redirect('accept')

    return render(req,"accept.html")

def home(req):
    return render(req,"home.html")

def resume(req, id):
    userProfile = Profile.objects.get(pk = id)
    print(userProfile.name)
    return render(req, "resume.html", {'userProfile':userProfile})