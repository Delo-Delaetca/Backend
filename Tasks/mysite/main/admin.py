from django.contrib import admin
from .models import User

# Особо пока не вдумывался
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass