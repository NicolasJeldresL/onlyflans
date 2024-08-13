from django.shortcuts import render
from .models import Flan
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ContactFormForm

from django.http import HttpResponse, JsonResponse

def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)

    return render(request, 'index.html', {'flanes': flanes_publicos})

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

