from django.contrib import admin
from .models import djangoTooDifficult

# Register your models here.

@admin.register(djangoTooDifficult)
class djangoTooDifficultAdmin(admin.ModelAdmin):
    pass

