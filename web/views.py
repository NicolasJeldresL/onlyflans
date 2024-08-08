from django.shortcuts import render

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def welcome(request):
    if request.user.is_authenticated:
        message = f"Bienvenido {request.user.username}"
    else:
        message = "Bienvenido cliente"
    return render(request, 'welcome.html', {'message': message})
