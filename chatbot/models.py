from django.db import models
from django.contrib.auth.models import User

class Conversation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='conversations')
    prompt = models.CharField(max_length=512)
    response = models.TextField()

    def __str__(self):
        return f"{self.prompt}: {self.response}"