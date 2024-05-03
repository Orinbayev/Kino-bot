from django.db import models

# Create your models here.

class MoviesModel(models.Model):
    kino_odi = models.CharField(max_length=100)
    qoshimcha = models.TextField()
   # photo = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True, blank=True)
    kod = models.IntegerField()
    silka = models.CharField(max_length=255)
    

    
    def __str__(self):
        return self.kino_odi
