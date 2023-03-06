from django.contrib import admin

# Register your models here.
from .models import text


@admin.register(text)
class TextAdmin(admin.ModelAdmin):
    pass
