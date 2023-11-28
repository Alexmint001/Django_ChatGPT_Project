from rest_framework.serializers import ModelSerializer, ReadOnlyField
from .models import Conversation

class ConversationSerializer(ModelSerializer):
    user = ReadOnlyField(source='user.username')
    class Meta:
        model = Conversation
        fields = '__all__'
        
        