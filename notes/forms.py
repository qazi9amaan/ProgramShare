from django import forms 
from .models import Material

class FeedForm(ModelForm):
    class Meta:
        model=Feed
        fields=('text','auth','files')
        widgets={"files":forms.FileInput(attrs={'id':'files','required':True,'multiple':True})}