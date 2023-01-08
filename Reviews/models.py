from django.db import models

# Create your models here.
class Review(models.Model):
    # there is no need to name column as it is as field they can be different
    username = models.CharField(max_length=20)
    description = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return self.username


