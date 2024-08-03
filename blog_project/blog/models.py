# blog/models.py

from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return f"Contact from {self.email or self.phone_number}"
