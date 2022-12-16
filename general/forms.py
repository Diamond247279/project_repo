from django import forms
from django.forms import ModelForm
from .models import Repo


class RepoForm(ModelForm):
    class Meta:
        model = Repo
        fields = ('matric_no', 'year','project_title','document')

        
