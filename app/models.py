from django.db import models

# Create your models here.

class Skills(models.Model):
    name = models.CharField(max_length=300)
    skill_percent = models.IntegerField()

    class Meta:
        verbose_name = ("Skill")
        verbose_name_plural = ("Skills")

    def __str__(self):
        return f"{self.name} --- {self.skill_percent}"


class Service(models.Model):
    icon_name = models.CharField(max_length=45)
    name = models.CharField(max_length=100)
    description = models.TextField()
    

    class Meta:
        verbose_name = ("Service")
        verbose_name_plural = ("Services")

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
        return f"{self.course_Name} ----- {self.duration}"

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length= 300)
    image =models.ImageField(upload_to='ProjectImages/')
    languages = models.CharField(max_length= 500)
    previewlink = models.URLField()
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = ("Project")
        verbose_name_plural =("Projects")

    def __str__(self):
        return self.name


class Testimonial(models.Model):

    customerName = models.CharField(max_length=300)
    customerProfession = models.CharField(max_length=300)
    customerComment = models.TextField()
    customerImage = models.ImageField(upload_to='TestimonialsImg/')

    class Meta:
        verbose_name = ("Testimonial")
        verbose_name_plural = ("Testimonials")

    def __str__(self):
        return f"{self.customerName } ---- {self.customerProfession}" 


class Contacts(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Contact")
        verbose_name_plural = ("Contacts")

    def __str__(self):
        return f"{self.name} --- {self.email}"

    


    
