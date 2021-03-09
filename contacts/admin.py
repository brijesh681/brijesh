from django.contrib import admin
from .models import contact

# Register your models here.
@admin.register(contact)
class contactadmin(admin.ModelAdmin):
    list_display = ('name','email','subject','message')
