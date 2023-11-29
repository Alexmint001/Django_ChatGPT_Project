from django.db import models
from django.contrib.auth.models import User

class MemoryCard(models.Model):
    '''
    MemoryCard 모델입니다.
    difficulty 필드는 사용하지 않습니다.
    '''
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    difficulty = models.ForeignKey('Difficulty', on_delete=models.SET_NULL, related_name='difficulties', null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    
    def __str__(self):
        return self.title
    
class Difficulty(models.Model):
    '''
    Difficulty 모델입니다.
    사용하지 않습니다.
    '''
    difficulty = models.CharField(max_length=20)
    
    def __str__(self):
        return self.difficulty