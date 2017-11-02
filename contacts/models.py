from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

class Client(models.Model):
    createur = models.ForeignKey('auth.User')
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    image = models.ImageField(upload_to='C:/Users/ssoumeya/djangogirls/media', blank = True)
    email = models.EmailField(max_length=254)
    phone_regex = RegexValidator(regex=r'd{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    telephone = models.CharField(validators=[phone_regex], max_length=15, blank=True) # validators should be a list
    facebook = models.CharField(max_length=200)
    whatsap = models.IntegerField()
    remarques = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    
    def __str__(self):
        return self.nom