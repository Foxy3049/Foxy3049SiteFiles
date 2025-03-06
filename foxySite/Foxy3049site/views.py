from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def games(request):
    return render(request, 'games.html')