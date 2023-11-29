from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    '''
    회원 가입 시리얼라이저
    profile_image는 사용하지 않습니다.
    username과 email은 회원가입시 필수로 입력이 필요하며 중복이 불가능합니다.
    password와 password2는 같은 값이여야하며 필수로 입력되어야 합니다.
    '''
    profile_image = serializers.ImageField(
        required = False,
        use_url=True
    )
    username = serializers.CharField(
        required = True,
        validators = [UniqueValidator(queryset=User.objects.all())] 
    )

    email = serializers.EmailField(
        required = True,
        validators = [UniqueValidator(queryset=User.objects.all())] 
    )
    password = serializers.CharField(
        write_only = True, 
        required = True, 
        validators = [validate_password]
    )
    password2 = serializers.CharField(
        write_only = True, 
        required = True
    )
    
    class Meta:
        model = User        
        fields = '__all__'

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': '비밀번호가 일치하지 않습니다.'})
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user
    
class LoginSerializer(serializers.ModelSerializer):
    '''
    로그인 시리얼라이저
    username과 password를 입력받고 email 필드를 같이 직렬화합니다.
    '''
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']




    