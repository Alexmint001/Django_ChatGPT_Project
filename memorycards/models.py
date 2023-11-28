from django.db import models
from django.contrib.auth.models import User

class MemoryCard(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    difficulty = models.ForeignKey('Difficulty', on_delete=models.SET_NULL, related_name='difficulties', null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    
    def __str__(self):
        return self.title
    
class Difficulty(models.Model):
    difficulty = models.CharField(max_length=20)
    
    def __str__(self):
        return self.difficulty