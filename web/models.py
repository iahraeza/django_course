from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    STATUS = (
        ('PUB', 'Published'),
        ('DRF', 'Draft'),
    )

    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=3, choices=STATUS)