from django.forms import ModelForm
from django import forms
from .models import Movie


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ('name', 'description', 'likes', 'language', 'watch_count', 'production_date', 'rate', 'actors', 'category', 'poster', 'video')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the movie name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'placeholder': 'Write the description of the movie'}),
            'likes': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of likes'}),
            'language': forms.SelectMultiple(attrs={'class': 'form-control ', 'size': '3', 'aria-label': 'size 3 select example'}),
            'watch_count': forms.NumberInput(attrs={'class': 'form-control'}),
            'production_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Example : 2021-11-08'}),
            'rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'actors': forms.SelectMultiple(
                attrs={'class': 'form-control ', 'size': '3', 'aria-label': 'size 3 select example'}),
            'category': forms.SelectMultiple(
                attrs={'class': 'form-control ', 'size': '3', 'aria-label': 'size 3 select example'}),
            'poster': forms.TextInput(attrs={'class': 'form-control h-100 mb-2 p-0 ', 'type': "file", 'id': "formFile"}),
            'video': forms.TextInput(attrs={'class': 'form-control h-100 mb-2 p-0 ', 'type': "file", 'id': "formFile"})
        }

# 'production_date': forms.DateTimeInput(attrs={'class': 'form-control'})
# 'video': forms.TextInput(attrs={'class': 'form-control h-100 mb-2 p-0 ', 'type': "file", 'id': "formFile"})