from django import forms
from django.forms import ModelForm
from .models import Academic_Division, Lab

#Create a Academic Division Form

class Academic_Division_Form(ModelForm):
	class Meta:
		model = Academic_Division
		# fields = "__all__"
		fields = ('name','acad_div_type', 'web', 'email')
		labels = {
			'name': '',
			'acad_div_type': '',
			'web': '',
			'email': '',
		}

		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}),
			'acad_div_type': forms.Select(attrs={'class':'form-select', 'placeholder':'Academic Division Type'}),
			'web': forms.URLInput(attrs={'class':'form-control', 'placeholder':'Website Address'}),
			'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email ID'}),
		}

class Lab_Form(ModelForm):
	class Meta:
		model = Lab
		# fields = "__all__"
		fields = ('name','academic_division','faculty', 'contact','web', 'email_address', 'associated_users', 'address', 'poc_manager', 'description','research_equipment')
		labels = {
			'name': '',
			'academic_division': 'Academic Division',
			'faculty': '',
			'contact': '',
			'web': '',
			'email_address': '',
			'associated_users':'Associated Users',
			'address': '',
			'poc_manager': 'PoC Manager',
			'description': '',
			'research_equipment': '',
		}

		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}),
			'academic_division': forms.Select(attrs={'class':'form-select', 'placeholder':'Academic Division'}),
			'faculty': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Associated Faculty'}),
			'contact': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Contact'}),
			'web': forms.URLInput(attrs={'class':'form-control', 'placeholder':'Website Address'}),
			'email_address': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email ID'}),
			'associated_users': forms.SelectMultiple(attrs={'class':'form-select', 'placeholder':'associated_users'}),
			'address': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}),
			'poc_manager': forms.Select(attrs={'class':'form-select', 'placeholder':'PoC manager'}),
			'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}),
			'research_equipment': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Research Equipment'}),
		}
