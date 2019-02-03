from django.contrib import admin
from crud.models import Empdtls

# Register your models here.

class EmpdtlsAdmin(admin.ModelAdmin):
	list_display = ('firstname', 'emp_id',)
	# class Meta:
	# 	model = Empdtls
	# 	list_display = ('lastname', 'emp_id',)	


admin.site.register(Empdtls,EmpdtlsAdmin)
