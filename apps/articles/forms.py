from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    model = Review
    fields = ['email','fio','review','rating','created_time']