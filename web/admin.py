from django.contrib import admin
from .models import Flan, Review
from .models import ContactForm

admin.site.register(Flan)
admin.site.register(Review)
admin.site.register(ContactForm)

