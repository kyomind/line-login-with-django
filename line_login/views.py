from django.shortcuts import render

# Create your views here.
def main(request):
    """首頁(登入頁面)
    """
    return render(request, 'index.html')