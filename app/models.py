from django.db import models

# Create your models here.

class Skills(models.Model):
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=500)
    skill_percent = models.CharField(max_length=5)

    class Meta:
        verbose_name = ("Skill")
        verbose_name_plural = ("Skills")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Skills_detail", kwargs={"pk": self.pk})

