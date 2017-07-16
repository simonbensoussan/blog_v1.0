from django.contrib import admin
from .models import Join
# Register your models here.

#custumer the admin interface

class JoinAdmin(admin.ModelAdmin):
    list_display = ['username','email','timestamp','update']
    class Meta:
        model = Join


admin.site.register(Join,JoinAdmin)