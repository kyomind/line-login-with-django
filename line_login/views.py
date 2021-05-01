from django.shortcuts import render, redirect
from .models import User


# Create your views here.
def main(request):
    """首頁(登入頁面)
    """
    content = User.objects.all()
    return render(request, 'main.html', locals())


def log_in(request):
    """登入頁面(轉址至LINE)
    """
    pass


def log_out(request):
    """登出
    """
    logout(request)
    return redirect('/')