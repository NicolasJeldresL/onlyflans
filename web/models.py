from django.db import models
import uuid
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')



    def __str__(self):
        return self.name

class Flan(models.Model):
    flan_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True)
    image_url = models.URLField()
    slug = models.SlugField(unique=True)
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()

    def __str__(self):
        return self.customer_name
    
class Review(models.Model):
    flan = models.ForeignKey(Flan, on_delete=models.CASCADE, related_name='reviews')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    calificacion = models.IntegerField(default=1)  # Rango de 1 a 5
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review de {self.usuario} para {self.flan}"