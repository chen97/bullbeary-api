from django.db import models


class Posts(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    content = models.TextField(blank=True, default='')
    owner = models.ForeignKey(
        'auth.User', related_name='posts', on_delete=models.CASCADE)
    views = models.IntegerField(blank=True, default=1)
    replies = models.IntegerField(blank=True, default=0)
    up_votes = models.IntegerField(blank=True, default=0)
    down_votes = models.IntegerField(blank=True, default=0)
    last_edit = models.DateTimeField(auto_now=True)
