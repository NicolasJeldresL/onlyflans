from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('acerca/', views.about, name='about'),
    path('bienvenido/', views.welcome, name='welcome'),
    path('contacto/', views.contact, name='contact'),
    path('exito/', views.success, name='success'),
    path('signup/', views.signup, name='signup'),
    path('flan/<int:flan_id>/', views.flan_detail, name='flan_detail'),
    path('faq/', views.faq, name='faq'),
    path('gallery/', views.gallery, name='gallery'),
    path('galeria/', views.galeria, name='galeria'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/', views.profile, name='profile'),
]
