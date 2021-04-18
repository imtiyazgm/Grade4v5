from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import EngWS, HinWS, AraWS, MatWS, SciWS, IssWS, UssWS

class EngWSForm(forms.ModelForm):
    
    class Meta:
        model = EngWS
        fields = ('Chapter', 'EngWSFile')

class HinWSForm(forms.ModelForm):
    
    class Meta:
        model = HinWS
        fields = ('Chapter', 'HinWSFile')

class AraWSForm(forms.ModelForm):
    
    class Meta:
        model = AraWS
        fields = ('Chapter', 'AraWSFile')

class MatWSForm(forms.ModelForm):
    
    class Meta:
        model = MatWS
        fields = ('Chapter', 'MatWSFile')

class SciWSForm(forms.ModelForm):
    
    class Meta:
        model = SciWS
        fields = ('Chapter', 'SciWSFile')


class IssWSForm(forms.ModelForm):
    
    class Meta:
        model = IssWS
        fields = ('Chapter', 'IssWSFile')


class UssWSForm(forms.ModelForm):
    
    class Meta:
        model = UssWS
        fields = ('Chapter', 'UssWSFile')
