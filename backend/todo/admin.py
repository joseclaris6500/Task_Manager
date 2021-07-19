from django.contrib import admin
from .models import Todo

class TododAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "completed")

#register modle
admin.site.register(Todo, TododAdmin)
