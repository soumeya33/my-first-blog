from django import forms

from .models import Client

class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ('nom', 'prenom', 'image', 'email', 'telephone', 'facebook','whatsap', 'remarques',)

       