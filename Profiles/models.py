from django.db import models

# Create your models here.

class UserProfile(models.Model):
    # create Data folder inside base MEDIA_ROOT folder and store images
    # Data folder is automatically created by Django
    # now it should only accept the images but is acceptiong other types of files
    # but form ImageField stops other types files
    image = models.ImageField(upload_to="Data")                 