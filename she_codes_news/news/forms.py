from django import forms
from django.forms import ModelForm
from .models import NewsStory


class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ["title", "category", "pub_date", "content", "story_image"]
        widgets = {
            "title": forms.TextInput(attrs={"class":"form-control"}),
            "category": forms.TextInput(attrs={"class":"form-control"}),
            "pub_date": forms.DateInput(format=("%m%d%Y"),
            attrs={"class": "form-control", "placeholder": "Select a date", "type": "date", "title": "Publication Date"}),
            "content": forms.Textarea(attrs={"class":"form-control"})
        }

