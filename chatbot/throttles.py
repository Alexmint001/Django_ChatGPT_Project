from rest_framework.throttling import UserRateThrottle

class ChatBotThrottle(UserRateThrottle):
    rate = '5/day'
    
    def allow_request(self, request, view):
        if request.method == 'POST':
            return super().allow_request(request, view)
        return
    