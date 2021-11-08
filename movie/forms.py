from django.forms import ModelForm
from django import forms
from .models import Movie


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ('name', 'description', 'likes', 'language', 'watch_count', 'rate', 'poster', 'video')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the movie name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'placeholder': 'Write the description of the movie'}),
            'likes': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Number of likes'}),
            'language': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the movie language'}),
            'watch_count': forms.TextInput(attrs={'class': 'form-control'}),
            # 'rate': forms.TextInput(attrs={'class': 'form-control'}),
            'poster': forms.TextInput(attrs={'class': 'form-control h-100 mb-2 p-0 ', 'type': "file", 'id': "formFile"}),
            'video': forms.TextInput(attrs={'class': 'form-control h-100 mb-2 p-0 ', 'type': "file", 'id': "formFile"})
        }

# 'production_date': forms.TextInput(attrs={'class': 'form-control'})
# 'video': forms.TextInput(attrs={'class': 'form-control h-100 mb-2 p-0 ', 'type': "file", 'id': "formFile"})