from django.db import models
from django.contrib.auth.models import User

class Conversation(models.Model):
    '''
    해당 채팅의 사용자 별로 채팅을 관리하기 위해 user 필드 추가함.
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='conversations')
    prompt = models.CharField(max_length=512)
    response = models.TextField()

    def __str__(self):
        return f"{self.prompt}: {self.response}"