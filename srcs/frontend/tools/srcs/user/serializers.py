from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
    def create(self, validated_data):
        user = User.objects.create_user(
			email = validated_data['email'],
			password = validated_data['password']
		)
        return user
    """
    유효성 검증을 통과한 validated_data를 이용하여 입력 값을 검증하고 유저 객체를 만든ㄷ.
    회원가입과 로그인도 똑같은 시리얼라이저를 사용하기 때문에 하나로 통일하였다(고함). # create 오버라이딩의 차이
    """
    