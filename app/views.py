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
        "skills":skills,
        "services":service,
        "education":education,
        "categories":category,
        "projects":projects,
        "testimonial":testimonials,
        "form": contactform,
    }
    return render(request,template_name,context)