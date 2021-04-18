from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import EngClassNotes, HinClassNotes, AraClassNotes, MatClassNotes, SciClassNotes, IssClassNotes,UssClassNotes

class EngClassNotesForm(forms.ModelForm):
    
    class Meta:
        model = EngClassNotes
        fields = ('Chapter', 'EngNotesFile')



class HinClassNotesForm(forms.ModelForm):
    
    class Meta:
        model = HinClassNotes
        fields = ('Chapter', 'HinNotesFile')


class AraClassNotesForm(forms.ModelForm):
    
    class Meta:
        model = AraClassNotes
        fields = ('Chapter', 'AraNotesFile')



class MatClassNotesForm(forms.ModelForm):
    
    class Meta:
        model = MatClassNotes
        fields = ('Chapter', 'MatNotesFile')

class SciClassNotesForm(forms.ModelForm):
    
    class Meta:
        model = SciClassNotes
        fields = ('Chapter', 'SciNotesFile')

class IssClassNotesForm(forms.ModelForm):
    
    class Meta:
        model = IssClassNotes
        fields = ('Chapter', 'IssNotesFile')


class UssClassNotesForm(forms.ModelForm):
    
    class Meta:
        model = UssClassNotes
        fields = ('Chapter', 'UssNotesFile')