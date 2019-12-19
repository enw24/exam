from django import forms
from .models import *


class Form(forms.ModelForm):
    class random:
        model = Clothes
        fields = ['name', 'hotel_Main_Img']