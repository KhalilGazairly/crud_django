from django.forms import ModelForm
from django import forms
from .models import Movie


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ('name', 'description', 'likes', 'watch_count', 'rate' )

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the movie name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'placeholder': 'Write the description of the movie'}),
            'likes': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Number of likes'}),
            'watch_count': forms.TextInput(attrs={'class': 'form-control'}),
            'rate': forms.TextInput(attrs={'class': 'form-control'}),
        }
