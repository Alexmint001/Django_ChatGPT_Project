from django.db import models
from django.contrib.auth.models import User

class CardUser(models.Model):
    '''
    해당 글의 작성자는 기본값으로 username으로 지정한다.
    nickname과 profile_image는 현재 쓰이지 않는 필드입니다.
    '''
    username = models.OneToOneField(User, on_delete=models.CASCADE, related_name='username_carduser')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_carduser')
    nickname = models.CharField(default = username, max_length=64)
    profile_image = models.ImageField(default='media/default_profile_image.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    
