from django.contrib.auth.models import User
from django.db import models
from comment.models import Comment

# Create your models here.
class Post(models.Model):
    post_id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.CharField(max_length=100)
    publication_date = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.title

class Interaction(models.Model):
    interaction_id = models.BigAutoField(primary_key=True)
    user = models.ManyToManyField(User, related_name='interactions')
    post = models.ManyToManyField(Post, related_name='interactions')
    interaction_type = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Interaction {self.interaction_id}'