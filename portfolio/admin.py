from django.contrib import admin
from .models import Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):

        list_display = ['name', 'email', 'time']
        search_fields = ['name', 'message']
        list_editable = ['name']
        ordering = ['time']


# put the Post class into the admin interface
admin.site.register(Contact,ContactAdmin)

