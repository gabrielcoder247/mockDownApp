from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from mockDownApp.models import YesNoBar

# class SignUpForm(UserCreationForm):
#     first_name = forms.CharField(max_length=100, help_text='Last Name')
#     last_name = forms.CharField(max_length=100, help_text='Last Name')
#     email = forms.EmailField(max_length=150, help_text='Email')


#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name',
# 'email', 'password1', 'password2',)




class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=30,  required=False, help_text='Optional.')
    username = forms.CharField(max_length=30,required=False, help_text='Optional.')
    email = forms.CharField(max_length=30,required=False, help_text='Optional.')
    password1 = forms.CharField(max_length=30,required=False, help_text='Optional.')
    password2 = forms.CharField(max_length=30,required=False, help_text='Optional.')




    class Meta:
        model = User
        fields = ('username', 'name', 'email',
                  'password1', 'password2')


class YesNoBarForm(forms.ModelForm):


    class Meta:
        model = YesNoBar
        # fields=['polling_unit_name', 'party_score', 'part_choices']
        fields=['user','name','category','yes_button_text','no_button_text','thank_you_toggler']


