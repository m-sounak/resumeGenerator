from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, render
from .models import Profile
from django.urls import reverse
from django.template import loader
import pdfkit
import io

#config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')

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
        n = profile.id
        print(n)
        urlRedirect = "download/" + n
        
        return redirect(urlRedirect)

    return render(req,"accept.html")

def home(req):
    return render(req,"home.html")

def resume(req, id):
    userProfile = Profile.objects.get(pk = id)
    '''
    template = loader.get_template("resume.html")
    html = template.render({'userProfile':userProfile})
    option = {
        'page-size' : 'Letter',
        'encoding' : 'UTF-8',
        'enable-local-file-access': None
    }
    #pdf = pdfkit.from_string(html, False, option, configuration=config)
    pdf = pdfkit.from_string(html, False, option)
    response = HttpResponse(pdf, content_type = 'application/pdf')
    response['Content-Disposition'] = 'attachment'
    return response
    '''
    return render(req, "resume.html", {'userProfile':userProfile})

def download(req, id):
    user = Profile.objects.get(pk = id)
    return render(req, "download.html", {'user':user})