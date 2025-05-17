from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from .models import Register

def index(request):
    return render(request, 'index.html')

def games(request):
    return render(request, 'games.html')

def guestbook(request):
    return render(request, 'guestBook.html')

def reg(request):
    if request.method == 'POST':
        email_request = request.POST.get('email')
        nickname_request = request.POST.get('nickname')
        password_request = request.POST.get('password')
        print(f"Получен email: {email_request}")
    return render(request, 'register.html')
def auth(request):
    return render(request, 'auth.html')

def test(request):
    return render(request, 'test.html')

def chat(request):
    return render(request, 'chat.html')