from django.contrib import admin
from users.models import Users
# Register your models here.

#admin.site.register(Users)

class UsersAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email',)

admin.site.register(Users, UsersAdmin)
