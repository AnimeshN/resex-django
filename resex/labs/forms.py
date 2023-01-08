from django import forms
from django.forms import ModelForm
from .models import Academic_Division

#Create a Academic Division Form
class Academic_Division_Form(ModelForm):
	class Meta:
		model = Academic_Division
		# fields = "__all__"
		fields = ('name','acad_div_type', 'web', 'email')
		labels = {
			'name': '',
			'acad_div_type': 'Type  of Academic Division',
			'web': '',
			'email': '',
		}

		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}),
			'acad_div_type': forms.Select(attrs={'class':'form-select', 'placeholder':'Academic Division Type'}),
			'web': forms.URLInput(attrs={'class':'form-control', 'placeholder':'Website Address'}),
			'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email ID'}),
		}