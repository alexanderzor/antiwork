from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField


class Company(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/', blank=True)
    url = models.URLField()
    short_description = RichTextField(blank=True)
    description = RichTextField(blank=True)
    city = models.CharField(max_length=20)
    keywords = models.TextField(blank=True)

    def __str__(self):
        return self.title


class New(models.Model):
    title = models.CharField(max_length=400)
    content1 = RichTextField(blank=True)
    content2 = RichTextField(blank=True)
    date = models.DateField(default=timezone.now())


class Comment(models.Model):
    author = models.CharField(max_length=20)
    date = models.DateField(default=timezone.now())
    content = models.TextField()
    parent = models.ForeignKey(New)


class Feedback(models.Model):
    first_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    message = models.TextField()
    file = models.FileField(upload_to='files/', blank=True)
    company = models.ForeignKey(Company, related_name='feedbacks')
    date = models.DateField(default=timezone.now())

    def __str__(self):
        return self.email

