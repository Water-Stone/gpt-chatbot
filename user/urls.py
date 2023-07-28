from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    # user/
    # 회원가입
    path('signup/', views.Signup.as_view(), name='signup'),
    # 로그인
    path('login/', views.Login.as_view(), name='login'),
    # 로그아웃
    path('logout/', views.Logout.as_view(), name='logout'),
    # 회원탈퇴
    path('delete/', views.Delete.as_view(), name='delete'),
]