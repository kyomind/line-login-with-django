from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from allauth.socialaccount.models import SocialAccount

from .models import User


# Create your views here.
@login_required(login_url='log-in')
def main(request):
    """首頁(登入頁面)
    """
    social_user = SocialAccount.objects.get(user=request.user)
    provider = social_user.provider
    items = social_user.extra_data.items()


    return render(request, 'main.html', locals())


def log_in(request):
    """登入頁面
    """
    return render(request, 'login.html')


def log_out(request):
    """登出
    """
    logout(request)
    return redirect('/')