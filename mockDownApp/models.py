from django.db import models
from django.contrib.auth.models import User
from colorfield.fields import ColorField

# Create your models here.



class YesNoBar(models.Model):

    name = models.CharField(max_length=255,null=True)
    category = models.CharField(max_length=100,null=True)
    yes_button_text = models.CharField(max_length=100,blank=True, null=True)
    yes_button_bg_color = ColorField(format='hexa')
    no_button_text = models.CharField(max_length=70,blank=True, null=True)
    no_button_bg_color = ColorField(format='hexa')
    question = models.CharField(max_length=255, blank=True, null=True)
    thank_you_toggle = models.BooleanField(max_length=255, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True,null=True, related_name='user_booking')



    def save_user(self):
        self.save()

    def __str__(self):
        return self.name

