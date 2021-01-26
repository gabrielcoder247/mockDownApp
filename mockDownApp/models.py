from django.db import models
from django.contrib.auth.models import User
from colorfield.fields import ColorField

# Create your models here.



class YesNoBar(models.Model):

    COLOR_CHOICES = [
        ("#FFFFFF", "white"),
        ("#000000", "black")
    ]

    name = models.CharField(max_length=255,null=True)
    category = models.CharField(max_length=100,null=True)
    yes_button_text = models.CharField(max_length=100,blank=True, null=True)
    yes_button_bg_color = ColorField(choices=COLOR_CHOICES)
    no_button_text = models.CharField(max_length=70,blank=True, null=True)
    no_button_bg_color = ColorField(choices=COLOR_CHOICES)
    question = models.CharField(max_length=255, blank=True, null=True)
    thank_you_toggler = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True,null=True, related_name='user_booking')



    def save_user(self):
        self.save()

    def __str__(self):
        return self.name

