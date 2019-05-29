from django.db import models
from django.conf import settings

class Board(models.Model):
    title = models.CharField(max_length= 20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL , related_name = 'like_boards', blank= True)
    def __str__(self):
        return f'{self.id}번글 - {self.title}: {self.content}'

# Create your models here.
