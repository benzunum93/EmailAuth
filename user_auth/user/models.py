from django.db import models

# Create your models here.
class Album(models.Model):
    Album_name = models.CharField(max_length=200)
    Author = models.TextField()
        
    def __str__(self):      # If python2 use __str__ if python3
            
        return (self.post_heading)
