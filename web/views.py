from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

def index(request):
    postres = [
         {"name": "Tarta de chocolate", "description": "Deliciosa tarta de chocolate.", "url": "img/tartachocolate.jpg"},
        {"name": "Flan de Vainilla", "description": "Suave flan de vainilla.", "url": "img/flanvainilla.jpg"},
        {"name": "Tiramisu", "description": "Exquisito postre para el hogar.", "url": "img/tiramisu.jpg"},
    ]
    
    context = {
        'message': 'Bienvenidos a OnlyFlans!',
        'postres': postres,
    }
    
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def welcome(request):
    if request.user.is_authenticated:
        message = f"Bienvenido {request.user.username}"
    else:
        message = "Bienvenido cliente"
    return render(request, 'welcome.html', {'message': message})
