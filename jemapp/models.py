from django.db import models

# Create your models here.

class Mail(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return self.name