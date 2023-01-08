from django.contrib import admin
from .models import Academic_Division
from .models import ResExUser
from .models import Lab

# Register your models here.
#admin.site.register(Academic_Division)
admin.site.register(ResExUser)
#admin.site.register(Lab)

@admin.register(Academic_Division)
class Academic_DivisionAdmin(admin.ModelAdmin):
	list_display = ('name', 'acad_div_type', 'web')
	ordering = ('name',)
	search_fields = ('name','acad_div_type') #todo:search by acad_div_type

@admin.register(Lab)
class LabAdmin(admin.ModelAdmin):
	fields = (('name','academic_division'), ('contact', 'email_address'),('poc_manager','web'),'description', 'faculty', 'associated_users','address')
	list_display = ('name', 'academic_division', 'web', 'contact', 'poc_manager')
	list_filter = ('academic_division','poc_manager')
	ordering = ('name',)
	search_fields  = ('name', 'academic_division__name')
