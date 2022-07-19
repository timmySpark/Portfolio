from django.shortcuts import render , redirect
from app.models import *
from app.forms import *


# Create your views here.

def Home(request):
    template_name = "index.html"
    skills = Skills.objects.all().order_by('-skill_percent')
    service = Service.objects.all()
    education = Education.objects.all()
    category = Category.objects.all()
    projects = Project.objects.all()
    testimonials = Testimonial.objects.all()
    contactform = ContactForm()
    if request.method == 'POST':
        contactform = ContactForm(request.POST or None)
        if contactform.is_valid():
            contactform.save()
            return redirect('/')
        else:
            contactform.add_error("email", "please try again")
            
    else:
        contactform = ContactForm()       
    
    context = {
        "title":"Erinle Timilehin",
        "about":"I am a Detail-oriented , organized and meticulous Software Engineer with background working productivity in dynamic environments. Fluent in JavaScript , Kotlin and Python programming languages used to develop software within the tech industry , I work at a fast pace to meet tight deadlines. I'm also a Sports Lover , i play football , Table tennis , i also like photography  and i play musical instruments.",
        "skills":skills,
        "services":service,
        "education":education,
        "categories":category,
        "projects":projects,
        "testimonial":testimonials,
        "form": contactform,
    }
    return render(request,template_name,context)
    