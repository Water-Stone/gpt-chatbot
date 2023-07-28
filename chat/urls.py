from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    # chat/
    # 채팅 내역
    path('list/', views.List.as_view(), name='list'),
    # 채팅 요청
    # 채팅 응답
]