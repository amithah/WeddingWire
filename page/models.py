from django.db import models
from accounts.models import CustomUser


class Page(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="page")
    email = models.CharField(max_length=30, unique=True)
    groom_name = models.CharField(max_length=64)
    bride_name = models.CharField(max_length=64)
    DESIGN_CHOICES = [
        ('DESIGN_1', 'Design 1'),
        ('DESIGN_2', 'Design 2'),
        ('DESIGN_3', 'Design 2'),
        ('DESIGN_4', 'Design 4'),
    ]
    design = models.CharField(choices=DESIGN_CHOICES, max_length=10, default='Design 1')
    city = models.CharField(max_length=64)
    date = models.DateField()
    slug = models.CharField(max_length=255)

    def __str__(self):
        return self.email


class Image(models.Model):
    page = models.OneToOneField(Page, on_delete=models.CASCADE, related_name="images")
    bride_image = models.ImageField(default='woman1.jpg')
    groom_image = models.ImageField(default='groom.jpg')



