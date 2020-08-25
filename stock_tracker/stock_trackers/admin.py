from django.contrib import admin

# Register your models here.

from .models import Stock, Entry

admin.site.register(Stock)
admin.site.register(Entry)

