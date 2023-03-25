from django.contrib import admin
from accounts.models import Account
from django.contrib.auth.admin import UserAdmin


class AccAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')
    list_filter = ('id', 'username', 'email')
    search_fields = ('username', 'email')
    fields = ('username', 'email')
    readonly_fields = ('id',)


admin.site.register(Account, UserAdmin)


