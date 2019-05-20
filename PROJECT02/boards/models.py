from django.db import models

class Board(models.Model):
    title= models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.id}번글 - {self.title}: {self.content}'
    
class Comment(models.Model):
    content = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)
    board = models.ForeignKey(Board, on_delete = models.CASCADE)
    
    def __str__(self):
        return f'<Board({self.board_id}): Comment({self.id})>'
        
# after add models.py, makemigrations and migrate