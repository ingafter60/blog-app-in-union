from django.contrib import admin
from .models import *

"""
Modify admin panel display
1. Add search field - The value of 'search_fields' must be a list or tuple.
2. Add list_display - The value of 'list_display' must be a list or tuple.
"""
class CategoriaAdmin(admin.ModelAdmin):
	search_fields = ['nomber']
	list_display  = ('nombre', 'fecha_creacion',  'estado')

class AutorAdmin(admin.ModelAdmin):
	search_fields = ['nombres', 'apellidos', 'correo']
	list_display  = ('nombres', 'estado', 'correo', 'fecha_creacion', 'estado')	

# Register models and admin-class
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)
