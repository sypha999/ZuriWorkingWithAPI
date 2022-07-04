from django.db import models
from cgitb import text
from turtle import title
from django.template.defaultfilters import slugify
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
class Link():
    target_url=models.URLField(max_length=200)
    description=models.CharField(max_length=200)
    identifier=models.SlugField(max_length=20,blank=True,unique=True)
    author=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    created_date=models.DateTimeField()
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.target_url

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        pass
     