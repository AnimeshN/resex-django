from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
# from django.contrib.auth.decorators import login_required

# Create your views here.

# @login_required(login_url="login")

def register_user(request):
	if request.method == "POST":
		username = request.POST.get('username')
		email = request.POST.get('email')
		password1 = request.POST.get('password1')
		password2 = request.POST.get('password2')
		first_name = request.POST.get('first')
		last_name = request.POST.get('last')

		try:
			if password1 != password2:
				messages.success(request, "Passwords don't match.")
				return redirect('register-user')

			if User.objects.filter(username = username).first():
				messages.success(request, 'Username is taken.')
				return redirect('register-user')

			if User.objects.filter(email = email).first():
				messages.success(request, 'Email is taken.')
				return redirect('register-user')

			if "@iitb.ac.in" not in email:
				messages.success(request, 'The email should be an iitb email address.')
				return redirect('register-user')
			

			user_obj = User(username = username, email = email, first_name = first_name, last_name = last_name)
			user_obj.set_password(password1)
			user_obj.save()


			auth_token = str(uuid.uuid4())
			profile_obj = Profile.objects.create(user = user_obj, auth_token = auth_token)
			profile_obj.save()
			send_verification_mail(request,email,auth_token)
			messages.success(request, 'We have sent an email to verify your email address. Please check your mail for further steps.')
			return redirect('home')	

		except Exception as e:
			print(e)

	return render(request,'authenticate/register_user.html', {})

	# if request.method == "POST":
	# 	form = RegisterUserForm(request.POST)
	# 	if form.is_valid():
	# 		form.save()
	# 		username = form.cleaned_data["username"]
	# 		password = form.cleaned_data["password1"]
	# 		user = authenticate(username=username, password=password)
	# 		login(request, user)
	# 		messages.success(request, ("Registration successful."))
	# 		return redirect('home')

	# else:
	# 	form = RegisterUserForm()


	# return render(request,'authenticate/register_user.html', {'form':form,
	# 	})

def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user_obj = User.objects.filter(username = username).first()
		if user_obj is None:
			messages.success(request, ("Username not found."))
			return redirect('login')
		
		profile_obj = Profile.objects.filter(user = user_obj).first()

		if not profile_obj.is_verified:
			messages.success(request, ('We have sent an email to verify your email address. Please check your mail for further steps.'))
			return redirect('login')


		user = authenticate(request, username=username, password=password)
		if user is None:
			messages.success(request, ("Wrong Password. Try again"))
			return redirect('login')
		login(request, user)
		# Redirect to a success page.
		messages.success(request, ("You are logged in."))
		return redirect('home')

	else:	
		return render(request, 'authenticate/login.html', {})

def success(request):
	return render(request, "authenticate/success.html")
		

def logout_user(request):
	logout(request)
	messages.success(request, ("You were logged out."))
	return redirect('home')


def send_verification_mail(request, email, token):
	subject = "Your ResEx account needs verification."
	domain_name = get_current_site(request).domain
	link = f'http://{domain_name}/members/verify/{token}.'
	message = f"Hi! Please click on this {link} to verify your account."
	email_from = settings.EMAIL_HOST_USER
	recipient_list = [email]
	send_mail(subject, message, email_from, recipient_list)

def verify(request, auth_token):
	try:
		profile_obj = Profile.objects.filter(auth_token = auth_token).first()

		if profile_obj :
			if profile_obj.is_verified:
				messages.success(request, ("Your email has already been verified. Please login."))
				return redirect('login')

			profile_obj.is_verified = True
			profile_obj.save()
			messages.success(request, ("Your email has been verified. Please login."))
			return redirect('login')
		else:
			return redirect('/error')
	except Exception as e:
		print(e)

def error_page(request):
	return render(request, 'authenticate/error.html')
