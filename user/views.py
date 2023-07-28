from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .forms import SignupForm, LoginForm

class Signup:
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('blog:list')
        # 회원가입 페이지
        # 정보를 입력할 폼을 보여주어야 한다.
        form = SignupForm()
        context = {
            'form': form,
            'title': 'User'
        }
        return render(request, 'user/signup.html', context)
    
    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('user:login')
        context = {
            'form': form
        }
        return render(request, 'user/signup.html', context)

### Login
class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('blog:list')
        
        form = LoginForm()
        context = {
            'form': form,
            'title': 'User'
        }
        return render(request, 'user/user_login.html', context)
        
    def post(self, request):
        if request.user.is_authenticated:
            return redirect('blog:list')
        
        form = LoginForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password) # True, False
            
            if user:
                login(request, user)
                return redirect('blog:list')
            
        form.add_error(None, '아이디가 없습니다.')
        
        context = {
            'form': form
        }
        
        return render(request, 'user/user_login.html', context)


### Logout
class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('blog:list')


class Delete(APIView):
    def post(self, request):
        user = User.objects.get(user=request.user)
        # user.is_active = False
        return Response({'msg': 'Profile deleted'}, status=status.HTTP_200_OK)