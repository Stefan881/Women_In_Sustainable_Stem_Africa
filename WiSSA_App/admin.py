from django.contrib import admin
from .models import SubscribedUsers,Post


class SubscribedUsersAdmin(admin.ModelAdmin):
    list_display = ('email','created_date')

# Register your models here.


admin.site.register(SubscribedUsers,SubscribedUsersAdmin)
admin.site.register(Post)
