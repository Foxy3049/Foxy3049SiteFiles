from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def games(request):
    return render(request, 'games.html')

def guestbook(request):
    return render(request, 'guestBook.html')

def register(request):
    return render(request, 'register.html')

def reg(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print(f"Получен email: {email}")
    return render(request, 'register.html')