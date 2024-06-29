from django import forms
from .models import File

class FileForm(forms.ModelForm):
    matiere = forms.ChoiceField(choices=File.matiere_choix, required=False)
    niveau = forms.ChoiceField(choices=File.niveau_choix, required=False)
    class Meta:
        model = File
        fields = ['caption', 'file', 'matiere', 'niveau']

