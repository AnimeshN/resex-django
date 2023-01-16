from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core import validators


class RegisterUserForm(UserCreationForm):
	email = forms.EmailField(required=True, initial="@iitb.ac.in", widget=forms.EmailInput(attrs={'class':'form-control'}))
	first_name = forms.CharField(max_length=64, widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(max_length=64, widget=forms.TextInput(attrs={'class':'form-control'}))
	#academic_division = forms.CharField(max_length=128)

	def clean_email(self):
		email_cleaned = self.cleaned_data['email']
		if "@iitb.ac.in" not in email_cleaned:
			raise forms.ValidationError("Must be an IITB email address.")
		try:
			match = User.objects.get(email=email_cleaned)
		except User.DoesNotExist:
		# Unable to find a user, this is fine
			return email_cleaned

		# A user was found with this as a username, raise an error.
		raise forms.ValidationError('This email address is already registered.')


	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


	def __init__(self, *args, **kwargs):
		super(RegisterUserForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control' 
		self.fields['password1'].widget.attrs['class'] = 'form-control' 
		self.fields['password2'].widget.attrs['class'] = 'form-control' 