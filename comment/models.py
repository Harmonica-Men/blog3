from django.contrib.auth.models import User
from django.db import models

class Comment(models.Model):
    comment_id = models.BigAutoField(primary_key=True)
    post_id = models.CharField(max_length=255)
    users = models.ManyToManyField(User)
    content = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment {self.comment_id} on Post {self.post_id}'
        