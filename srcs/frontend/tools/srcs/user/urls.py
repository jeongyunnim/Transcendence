from django.urls import path
from .views import RegisterAPIView, AuthAPIView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
	path("regster/", RegisterAPIView.as_view()),
	path("auth/", AuthAPIView.as_view()),
	# post-login delete-logout get-유저정보 확인
	path("auth/refresh/", TokenRefreshView.as_view()) 
 	# jwt 토큰 재발급, simplejwt에서 제공하는 기능
]