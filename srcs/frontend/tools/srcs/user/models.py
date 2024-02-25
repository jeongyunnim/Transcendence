from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# helper class
class UserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        """
        주어진 이메일, 비밀번호 등 개인정보로 User 인스턴스 생성
        """
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
			email=email
		)
        user.set_password(password)
        user.save(using=self._db)
        return user
	# todo BaseUserManager이 뭐하는 클래스인지 알아보기
	
    def create_superuser(self, email=None, password=None, **extra_fields):
        """
        주어진 이메일, 비밀번호 등 개인정보로 User 인스턴스 생성
        최상위 사용자 권한 부여
        """
        superuser = self.create_user(
			email=email,
			password=password
		)
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.is_active = True
        
        superuser.save(using=self._db)
        return superuser

# AbstractBaseUser를 상속하여 유저 커스텀
# todo 두 개의 클래스를 상속하는 것에 대해 알아보자
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=30, unique=True, null=False, blank=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # 헬퍼 클래스 사용
    objects = UserManager()
    
    # 사용자의 username 필드는 email로 설정(email로 로그인)
    USERNAME_FIELD = 'email'
    """
	AbstractBaseUser 모델을 상속한 User 커스텀 모델은 로그인 아이디로 이메일 주소를 사용하거나 Django 로그인 절차가 아닌 다른 인증 절차를 직접 구현할 수 있다.
	PermissionMixin을 다중 상속하면 Django의 기본 그룹, 허가원 관리 기능을 재사용할 수 있다(고 한다).
	
	유저 생성은 UserManager(헬퍼 클래스)를 통해 이루어진다.
	일반 사용자 계정은 create_user
	관리자 계정은 create_superuser
 	"""
