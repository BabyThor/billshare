from django.contrib import admin

from .models import Bill, Item

admin.site.register(Bill)
admin.site.register(Item)
# Register your models here.
