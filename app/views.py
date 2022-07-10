from django.shortcuts import render , redirect
from app.models import *
from app.forms import *


# Create your views here.

def Home(request):
    template_name = "index.html"
    skills = Skills.objects.all()
    education = Education.objects.all()
    testimonials = Testimonial.objects.all()
    contactform = ContactForm()
    if request.method == 'POST':
        contactform = ContactForm(request.POST or None)
        if contactform.is_valid():
            contactform.save()
            
    
    context = {
        "skills":skills,
        "education":education,
        "testimonial":testimonials,
        "form": contactform,
    }
    return render(request,template_name,context)