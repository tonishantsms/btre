from django.contrib import admin

# Register your models here.

from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listings', 'email', 'contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'listings', 'email')
    list_per_pages = 25

admin.site.register(Contact,ContactAdmin )