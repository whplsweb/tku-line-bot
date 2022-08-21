from django.contrib import admin
from api.models import User

class user_Admin(admin.ModelAdmin):
    list_display = ('uid', 'name')

admin.site.register(User, user_Admin)