from rest_framework.views import APIView
from .serializers import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.shortcuts import render, get_object_or_404
from frontend.settings import SECRET_KEY
import jwt

class RegisterAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        # todo UserSerializer는 무엇인가
        if serializer.is_valid():
            user = serializer.save()
            
            # jwt 접근
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            res = Response(
				{
					"user": serializer.data,
					"message": "register sucess",
					"token": {
						"access": access_token,
						"refresh": refresh_token,
					},
				},
			)
            
            # jwt를 쿠키에 저장함.
            res.set_cookie("access", access_token, httponly=True)
            res.set_cookie("refresh", refresh_token, httponly=True)
            
            return res
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""
시리얼라이저를 사용하여 유저를 저장한다. == 회원가입
jwt 토큰을 받아 쿠키에 저장한다.
httponly dhqtusdms JS 스크립트 파일을 통해 쿠키를 조회할 수 없게 하기 위함이다.
XSS로부터 안전해지지만 CSRF로 부터 취약해지기 때문에 CSRF토큰을 함께 사용해야 한다.
"""

class AuthAPIView(APIView):
    # 유저 정보 확인
    def get(self, request):
        try:
            # access token을 decode하여 유저 id 추출
            access = request.COOKIES['acess']
            payload = jwt.decode(access, SECRET_KEY, algoritms=['HS256'])
            pk = payload.get('user_id')
            user = get_object_or_404(User, pk=pk)
            serializer = UserSerializer(instance=user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except(jwt.exceptions.ExpiredSignatureError):
            # 토큰 만료 시 토큰 갱신
            data = {'refresh': request.COOKIES.get('refresh', None)}
            serializer = TokenRefreshSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                access = serializer.data.get('access', None)
                refresh = serializer.data.get('refresh', None)
                payload = jwt.decode(access, SECRET_KEY, algorithms=['HS256'])
                pk = payload.get('user_id')
                user = get_object_or_404(User, pk=pk)
                serializer = UserSerializer(instance=user)
                res = Response(serializer.data, status=status.HTTP_200_OK)
                res.set_cookie('access', access)
                res.set_cookie('refresh', refresh)
                return res
            return jwt.exceptions.InvalidTokenError
        except(jwt.exceptions.InvalidTokenError):
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    # 로그인
    def post(self, request):
        # 유저 인증
        user = authenticate(
            email=request.data.get('email'), password = request.data.get('password')
        )
        # 이미 가입된 유저
        if user is not None:
            serializer = UserSerializer(user)
            # jwt 토큰 접근
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            res = Response(
                {
                    "user": serializer.data,
                    "message": "login success",
                    "token": {
                        "access": access_token,
                        "refresh": refresh_token,
                    },
                },
                status = status.HTTP_200_OK
            )
            # jwt를 쿠키에 저장함.
            res.set_cookie("access", access_token, httponly=True)
            res.set_cookie("refresh", refresh_token, httponly=True)
            return res
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    # 로그아웃
    def delete(self, request):
        # 쿠키에 저장된 토큰 삭제 == 로그아웃 처리
        response = Response(
            {
                "message": "Logout success"
            },
            status=status.HTTP_202_ACCEPTED                   
        )
        response.delete_cookie("access")
        response.delete_cookie("refresh")
        return response
"""
API View 하나에 메소드를 분리하여 구현
로그인은 회원과입과 시리얼라이저를 save하거나 get하거나의 차이만 있으며 jwt 토큰에 접근하여 쿠키에 저장하는 것은 동일.

유저 정보는 authorization에서 jwt 토큰을 포함시키지 않더라도 쿠키에 저장된 토큰으로 사용자의 정보를 보여준다.
"""

"""
[JWT 로그아웃]
JWT는 서버쪽에서 로그아웃을 할 수 없다.
한 번 발근된 JWT 토큰을 강제로 삭제하거나 무효화할 수 없음
-> JWT 토큰의 유효기간을 짧게 하거나, 토큰을 DB에 보존하고 매 요청마다 DB에 존재하는 토큰인지 확인한다.
-> 유저측에서 쿠키를 삭제하면 서버에서 유저를 확인할 방법이 없다.
"""

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer