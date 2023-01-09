from django.db import models
from django.contrib.auth.models import User


class Academic_Division(models.Model):
	DEPARTMENT = 'Department'
	SCHOOL = 'School'
	INTERDISCIPLINARY_PROGRAM = 'Interdisciplinary Program'
	CENTRE = 'Centre'

	acad_div_type_CHOICES = [(DEPARTMENT, 'Department'),(SCHOOL, 'School'),	(INTERDISCIPLINARY_PROGRAM, 'Interdisciplinary Program'),(CENTRE, 'Centre'),]
	name = models.CharField('Academic Division Name', max_length=256)
	acad_div_type = models.CharField('Academic Division Type',max_length=28,choices=acad_div_type_CHOICES,default=DEPARTMENT,) # Dept, school, IDP, centers
	web = models.URLField('Website address')
	email = models.EmailField('Email Address', max_length=128, blank=True)
	
	# Below part allows you to access DB from admin page
	def __str__(self):
		return self.name

class ResExUser(models.Model):
	first_name = models.CharField(max_length=60)
	last_name = models.CharField(max_length=50)
	email = models.CharField('User Email', max_length=128)
	
	# Below part allows you to access DB from admin page
	def __str__(self):
		return self.first_name + ' ' + self.last_name


class Lab(models.Model):
	name = models.CharField('Lab Name', max_length=256)
	academic_division = models.ForeignKey(Academic_Division, blank=True, null=True, on_delete=models.SET_NULL)
	faculty = models.CharField('Faculty associated', blank=True, max_length=256) 
	contact = models.CharField('Contact number', max_length=256, blank=True)
	#photo = models.ImageField()
	description = models.TextField(blank=True)
	research_equipment = models.TextField(blank=True)
	web = models.URLField('Website address', blank=True)
	email_address = models.EmailField('Email Address', max_length=128, blank=True)
	associated_users = models.ManyToManyField(ResExUser, blank=True) 
	address = models.CharField('Address', max_length=256, blank=True)
	poc_manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

	# Below part allows you to access DB from admin page
	def __str__(self):
		return self.name
