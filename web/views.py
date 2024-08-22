from django.shortcuts import render, redirect, get_object_or_404
from .models import Flan
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ContactFormForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login
from .forms import SignUpForm

def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, 'index.html', {'flanes': flanes_publicos})

@login_required
def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(request, 'welcome.html', {'flanes': flanes_privados})

def success(request):
    return render(request, 'success.html')

def contact(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('success'))
    else:
        form = ContactFormForm()
    return render(request, 'contactus.html', {'form': form})

def about(request):
    return render(request, 'about.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def flan_detail(request, flan_id):
    flan = get_object_or_404(Flan, id=flan_id)
    reviews = flan.reviews.all()  # Obtiene todas las reseñas del flan
    return render(request, 'flan_detail.html', {'flan': flan, 'reviews': reviews})

def faq(request):
    return render(request, 'faq.html')

def galeria(request):
    return render(request, 'galeria.html')
