from django.shortcuts import render
import calendar 
from calendar import HTMLCalendar
from datetime import datetime
from .models import Lab, Academic_Division
from .forms import Academic_Division_Form
from django.http import HttpResponseRedirect


# Create your views here.

def show_acad_div(request, acad_div_id):
	acad_div = Academic_Division.objects.get(pk=acad_div_id)
	return render(request, 'labs/acad_div.html',
		{'acad_div':acad_div})

def list_acad_divs(request):
	acad_div_list = Academic_Division.objects.all()
	return render(request, 'labs/acad_div_list.html',
		{'acad_div_list':acad_div_list})

def all_labs(request):
	lab_list = Lab.objects.all()
	return render(request, 'labs/lab_list.html',
		{'lab_list':lab_list})


def home(request, year=datetime.now().year, month=datetime.now().strftime("%B")):
	name="Yash"
	# Convert month from name to number
	month = month.capitalize() 
	month_number = list(calendar.month_name).index(month)
	month_number = int(month_number)

	# create a calendar
	cal = HTMLCalendar().formatmonth(year, month_number)

	# get the current year
	now = datetime.now()
	current_year = now.year

	# get current time
	time = now.strftime("%I:%M %p")

	return render(request, 
		'labs/home.html', {
		"name" : name, 
		"year" : year,
		"month" : month,
		"month_number" : month_number,
		"cal" : cal,
		"current_year" : current_year,
		"time" : time,
		})

def add_acad_div(request):
	submitted = False
	if request.method == "POST":
		form = Academic_Division_Form(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/add_acad_div?submitted=True')
	else:
		form = Academic_Division_Form
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'labs/add_acad_div.html', {'form':form, 'submitted':submitted})

