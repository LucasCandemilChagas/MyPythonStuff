from django.contrib import admin

from . import models

# Register your models here.
class NotaAdmin(admin.ModelAdmin):
    list_display = ('title',)
    
admin.site.register(models.Nota, NotaAdmin)