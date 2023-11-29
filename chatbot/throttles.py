from rest_framework.throttling import UserRateThrottle

class ChatBotThrottle(UserRateThrottle):
    '''
    post 요청에 대해서 인증된 사용자 요청은 1일 5회로 제한합니다.
    '''
    rate = '5/day'
    scope = 'post_user'
    def allow_request(self, request, view):
        if request.method == 'POST':
            return super().allow_request(request, view)
        return True
    