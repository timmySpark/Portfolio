from django.shortcuts import render
from app.models import *


# Create your views here.

def Home(request):
    template_name = "index.html"
    skills = Skills.objects.all()
    education = Education.objects.all()
    testimonials = Testimonial.objects.all()
    context = {
        "skills":skills,
        "education":education,
        "testimonial":testimonials,
    }
    return render(request,template_name,context)