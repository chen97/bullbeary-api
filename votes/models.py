from django.db import models
from posts.models import Posts
from comments.models import Comments

# Create your models here.
class Votes(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    vote_sender = models.ForeignKey('auth.User', related_name='votes', on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, related_name='votes', on_delete=models.CASCADE, null=True)
    comment = models.ForeignKey(Comments, related_name='votes', on_delete=models.CASCADE, null=True)
    up_vote = models.BooleanField(blank=False, default=True)