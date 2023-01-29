from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def test(request):
    return render(request, 'test.html')

def cricket(request):
    return render(request, 'cricket.html')

def football(request):
    return render(request, 'football.html')

def table_tennis(request):
    return render(request, 'table_tennis.html')

def lawn_tennis(request):
    return render(request, 'lawn_tennis.html')
 
def volleyball(request):
    return render(request, 'volleyball.html')
 
def basketball(request):
    return render(request, 'basketball.html')
 
def badminton(request):
    return render(request, 'badminton.html')
 
def pool(request):
    return render(request, 'pool.html')
 
def carrom(request):
    return render(request, 'carrom.html')
 
def chess(request):
    return render(request, 'chess.html')
 
def athletics(request):
    return render(request, 'athletics.html')
 
def kabbadi(request):
    return render(request, 'kabbadi.html')
 
def karate(request):
    return render(request, 'karate.html')
 
def yoga(request):
    return render(request, 'yoga.html')
 
def online_games(request):
    return render(request, 'online_games.html')
 
def coremember(request):
    return render(request, 'coremember.html')
 
