from django.contrib import admin
from .models import Consumer,Producer, Product, Consumption, Transition, PastPrices

admin.site.register(Consumer)
admin.site.register(Producer)
admin.site.register(Product)
admin.site.register(Consumption)
admin.site.register(Transition)
admin.site.register(PastPrices)
