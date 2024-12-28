from django.db import models
from django.urls import reverse
# Create your models here.
class Carousel(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField()

    def __str__(self):
        return self.name


class About(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    img = models.ImageField(upload_to='about/')
    slug = models.SlugField(unique=True, blank=True)

    def get_absolute_url(self):
        return reverse("aboutDetailView", args=[self.slug])

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    img = models.ImageField(upload_to='room/')

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    img = models.ImageField(upload_to='testimonial/')

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    lavozim = models.CharField(max_length=100)
    img = models.ImageField(upload_to='team/')

    def __str__(self):
        return self.name

class Newsletter(models.Model):
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.email

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.name


