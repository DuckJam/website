from django.db import models

NAME_MAX_LENGTH = 128

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    def __str__(self):
        return self.title



class Page(models.Model):
    title = models.CharField(max_length=NAME_MAX_LENGTH)
    url = models.URLField()
    def __str__(self):
        return self.title
    
class Image(models.Model):
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    image = models.ImageField(upload_to='images')
    def __str__(self) -> str:
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=NAME_MAX_LENGTH)
    date = models.DateTimeField("date published")
    text = models.TextField()
    #image = models.ImageField(upload_to='images', blank=True)
    image = models.ManyToManyField(Image)
    def __str__(self):
        return self.title