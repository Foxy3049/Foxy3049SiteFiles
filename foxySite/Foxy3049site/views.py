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
        regs = Register(email=email_request, nickname=nickname_request, password=password_request, send_date = timezone.now())
        regs.save()
        print(f"Получен email: {email_request}")
        return JsonResponse({'status': 'success', 'message': 'Так ага ага... О. Данные поступает.. Так так... Записываю, записываю...'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Где данные ёмаё'})
    return render(request, 'register.html')
