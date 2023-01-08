from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class Review(models.Model):
    # there is no need to name column as it is as field they can be different
    # right now we are using ModelForm which is not limiting the data user entered
    username = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    def __str__(self):
        return self.username


