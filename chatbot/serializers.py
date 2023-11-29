from rest_framework.serializers import ModelSerializer, ReadOnlyField
from .models import Conversation

class ConversationSerializer(ModelSerializer):
    '''
    user 필드를 사용할 때 값은 user의 username을 사용합니다.
    '''
    user = ReadOnlyField(source='user.username')
    class Meta:
        model = Conversation
        fields = '__all__'
        
        