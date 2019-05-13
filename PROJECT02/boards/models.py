from django.db import models

class Board(models.Model):
    title= models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return f'{self.id}번글 - {self.title}: {self.content}'