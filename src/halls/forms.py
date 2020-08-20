from django import forms

from .models import Hall, Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'url', 'youtube_id']

class SearchForm(forms.Form):
    search = forms.CharField(max_length=255, label='Search Videos', widget=forms.TextInput(attrs={'class':'form-control'}))