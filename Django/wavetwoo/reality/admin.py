from django.contrib import admin

from .models import Cooktsu, Transmutation, Ingredient, Quantity

# Register your models here.
admin.site.register(Cooktsu)
admin.site.register(Transmutation)
admin.site.register(Ingredient)
admin.site.register(Quantity)
