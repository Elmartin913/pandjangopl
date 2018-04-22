from django.contrib import admin

from .models import Contact

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'message', 'email', 'mobile']
    list_filter = ('created',)
    search_fields = ('name', 'message')
    ordering = ['name', 'email']


