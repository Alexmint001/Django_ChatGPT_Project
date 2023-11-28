from rest_framework.serializers import ModelSerializer, ReadOnlyField, SerializerMethodField
from .models import MemoryCard

class MemoryCardSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.username')
    is_author = SerializerMethodField()
    
    class Meta:
        model = MemoryCard
        fields = '__all__'
    
    def get_is_author(self, obj):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            return obj.author == request.user
        return False