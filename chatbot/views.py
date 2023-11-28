from rest_framework.views import APIView
from rest_framework.response import Response
from dotenv import load_dotenv
from openai import OpenAI
import os
from .models import Conversation
from .serializers import ConversationSerializer
from rest_framework.permissions import IsAuthenticated
from .throttles import ChatBotThrottle

load_dotenv()
client = OpenAI(
    api_key=os.environ['OPENAI_API_KEY'],  
)

class ChatBotView(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [ChatBotThrottle]
    serializer_class = ConversationSerializer
    
    def get_queryset(self):
        return Conversation.objects.filter(user=self.request.user)
    
    def get(self, request, *args, **kwargs):
        conversations = self.get_queryset()
        serializer = ConversationSerializer(conversations, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        prompt = request.data.get('prompt')
        if prompt:
            # 이전 대화 기록 가져오기
            previous_conversations = self.get_queryset()
            previous_conversations_text = "\n".join([f"User: {c.prompt}\nAI: {c.response}" for c in previous_conversations])
            prompt_with_previous = f"{previous_conversations_text}\nUser: {prompt}\nAI:"
            
            model_engine = "text-davinci-003"
            completions = client.completions.create(
                model=model_engine,
                prompt=prompt_with_previous,
                max_tokens=1024,
                n=5,
                stop=None,
                temperature=0.5,
            )
            response = completions.choices[0].text.strip()
            
            serializer = ConversationSerializer(data={'prompt': prompt, 'response': response})
            if serializer.is_valid():
                serializer.save(user=self.request.user)
                return Response(serializer.data, status=201)

        return Response({"error": "Invalid input"}, status=400)
