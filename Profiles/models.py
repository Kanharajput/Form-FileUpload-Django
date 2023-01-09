from django.db import models

# Create your models here.

class UserProfile(models.Model):
    # create Data folder inside base MEDIA_ROOT folder and store images
    # Data folder is automatically created by Django
    image = models.FileField(upload_to="Data")                
