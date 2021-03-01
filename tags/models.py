from django.db import models
from posts.models import Posts

# Create your models here.
class Tags(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    owner = models.ForeignKey('auth.User', related_name='tags', on_delete=models.CASCADE)
    posts = models.ManyToManyField(Posts, related_name='tags', blank=True)

    class Meta:
        verbose_name_plural = 'tags'