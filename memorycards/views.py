from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import MemoryCard
from .serializers import MemoryCardSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOrReadOnly

class MemoryCardViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    '''
    1. CRUD 구현
    암기 카드 글 CRUD 기능 구현
    2. 계정관련
    로그인한 사용자만 READ(GET), CREATE(POST) 가능 IsAuthenticated
    작성자 본인일 경우에만 UPDATE(PUT), DELETE(DELETE) 가능 IsAuthorOrReadOnly
    '''
    queryset = MemoryCard.objects.all()
    serializer_class = MemoryCardSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({
            'request': self.request
        })
        return context
    
        
    
    
