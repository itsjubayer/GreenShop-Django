from django.contrib import admin
from .models import Product, Offer


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


#to customize column
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


admin.site.register(Offer, OfferAdmin)
#add ProductAdmin to register to customize columns for products admin panel
admin.site.register(Product, ProductAdmin)