from django import forms
from . import models
from django.contrib.auth.models import User





class userform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class profileform(forms.ModelForm):
        class Meta:
            model = models.Profile
            fields = ['prfile_image', 'country', 'address']

