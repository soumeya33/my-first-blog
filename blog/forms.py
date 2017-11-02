from django import forms

from .models import Importateur

class ImportateurForm(forms.ModelForm):

    class Meta:
        model = Importateur
        fields = ('matricule', 'description', 'email', 'telephone',)

       