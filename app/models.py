from django.db import models

# Create your models here.

class Skills(models.Model):
    name = models.CharField(max_length=300)
    skill_percent = models.IntegerField()

    class Meta:
        verbose_name = ("Skill")
        verbose_name_plural = ("Skills")

    def __str__(self):
        return self.name


class Education(models.Model):
    course_Name = models.CharField(max_length=500)
    school_Name = models.CharField(max_length=500)
    description = models.TextField()
    duration = models.CharField(max_length=500)
    
    class Meta:
        verbose_name = ("Education")
        verbose_name_plural = ("Educations")

    def __str__(self):
        return self.course_Name 

   
class Testimonial(models.Model):

    customerName = models.CharField(max_length=300)
    customerProfession = models.CharField(max_length=300)
    customerComment = models.TextField()
    customerImage = models.ImageField(upload_to='TestimonialsImg/')

    class Meta:
        verbose_name = ("Testimonial")
        verbose_name_plural = ("Testimonials")

    def __str__(self):
        return self.customerName 

    
