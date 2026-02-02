from django.db import models

# Create your models here.
class Design(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="hero_image/")
    is_active = models.BooleanField(default=True)
   

    class Meta:
        verbose_name = "Design"
        verbose_name_plural = "Designs"

    def __str__(self):
        return self.title
