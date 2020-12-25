# apps/blog/admin.py

from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Export-Import for Categoria
class CategoriaResource(resources.ModelResource):
	class Meta:
		model = Categoria

"""
Modify admin panel display
1. Add search field - The value of 'search_fields' must be a list or tuple.
2. Add list_display - The value of 'list_display' must be a list or tuple.
"""
class CategoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	search_fields = ['nomber']
	list_display  = ('nombre', 'fecha_creacion',  'estado')
	resource_class= CategoriaResource


# Export-Import for Autor
class AutorResource(resources.ModelResource):
	class Meta:
		model = Autor

class AutorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	search_fields = ['nombres', 'apellidos', 'correo']
	list_display  = ('nombres', 'correo', 'fecha_creacion', 'estado')	
	resource_class= AutorResource

# Register models and admin-class
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Post)
