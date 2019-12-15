from django.contrib import admin
from giftlistapp.models import Clothes, Jewelery, Vehicle, Pet, Other, Product

admin.site.register(Clothes)
admin.site.register(Jewelery)
admin.site.register(Vehicle)
admin.site.register(Pet)
admin.site.register(Other)
admin.site.register(Product)


def site(request):
    return None