from django.db import models
from django.template.defaultfilters import slugify
from datetime import datetime

NAME_MAX_LENGTH = 128

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    date = models.DateField("date started", null=True)
    description = models.TextField()
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)

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
    title = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    date = models.DateTimeField("date published", default = datetime.now)
    text = models.TextField()
    image = models.ManyToManyField(Image, null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank = True)
    visible = models.BooleanField(default=True)
    slug = models.SlugField(unique=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title