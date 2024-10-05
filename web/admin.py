from django.contrib import admin
from .models import Flan, Review
from .models import ContactForm
from .models import GalleryImage, FAQ
from .models import Image

class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'description')

class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')

class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_url')



admin.site.register(Flan)
admin.site.register(Review)
admin.site.register(ContactForm)
admin.site.register(GalleryImage)
admin.site.register(FAQ)
admin.site.register(Image, ImageAdmin)
