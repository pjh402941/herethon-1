from django.contrib import admin
from .models import User

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin) :
    list_display = ('username', 'name', 'email', 'nickname', 'school_name', 'school_photo', 'user_profile')
    exclude = ('password',)