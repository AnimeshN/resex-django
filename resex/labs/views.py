from django.shortcuts import render, redirect
import calendar 
from calendar import HTMLCalendar
from datetime import datetime
from .models import Lab, Academic_Division
from .forms import Academic_Division_Form, Lab_Form
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import csv
from django.core.paginator import Paginator


LABS_PER_PAGE = 1
AD_PER_PAGE = 1

# Create your views here.

# Generate a csv file lab list
def lab_csv(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename=labs.csv'

	# Create a CSV writer
	writer = csv.writer(response)

	# Designate the model
	labs = Lab.objects.all().order_by('name')

	# Add column headings to the csv file
	writer.writerow(['Lab Name', 'Academic Division', 'Associated Faculty', 'Contact', 'Description', 'Research Equipment', 'Website', 'Email', 'Associated Users', 'Address', 'Point of Contact/Manager'])


	# Loop through and output
	for lab in labs:
		writer.writerow([lab.name, lab.academic_division, lab.faculty, lab.contact, lab.description, lab.research_equipment, lab.web, lab.email_address, lab.associated_users, lab.address, lab.poc_manager])
	
	return response



# Delete a Academic Division
def delete_acad_div(request,acad_div_id):
	acad_div = Academic_Division.objects.get(pk=acad_div_id)
	acad_div.delete()

	return redirect('list-acad-divs')

# Delete a Lab
def delete_lab(request,lab_id):
	lab = Lab.objects.get(pk=lab_id)
	lab.delete()

	return redirect('list-labs')


def update_lab(request, lab_id):
	lab = Lab.objects.get(pk=lab_id)
	form = Lab_Form(request.POST or None, instance=lab)
	if form.is_valid():
		form.save()
		return redirect('list-labs')

	return render(request, 'labs/update_lab.html',
		{'lab':lab,
		'form':form})


def add_lab(request):
	submitted = False
	if request.method == "POST":
		form = Lab_Form(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/add_lab?submitted=True')
	else:
		form = Lab_Form
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'labs/add_lab.html', {'form':form, 'submitted':submitted})

def update_acad_div(request, acad_div_id):
	acad_div = Academic_Division.objects.get(pk=acad_div_id)
	form = Academic_Division_Form(request.POST or None, instance=acad_div)
	if form.is_valid():
		form.save()
		return redirect('list-acad-divs')

	return render(request, 'labs/update_acad_div.html',
		{'acad_div':acad_div,
		'form':form})


def search_acad_divs(request):
	if request.method == "POST":
		searched_acad_divs = request.POST.get('searched_acad_divs')
		acad_divs = Academic_Division.objects.filter(name__contains=searched_acad_divs)
		
		return render(request, 'labs/search_acad_divs.html',
		{'searched_acad_divs':searched_acad_divs,
		'acad_divs':acad_divs})
	else:
		return render(request,'labs/search_acad_divs.html')
		


def show_acad_div(request, acad_div_id):
	acad_div = Academic_Division.objects.get(pk=acad_div_id)
	return render(request, 'labs/acad_div.html',
		{'acad_div':acad_div})

def list_acad_divs(request):
	# Setup pagination
	pag = Paginator(Academic_Division.objects.all().order_by('name'), AD_PER_PAGE)
	page =request.GET.get('page')
	acad_divs = pag.get_page(page)
	nums = "a"*acad_divs.paginator.num_pages

	return render(request, 'labs/acad_div_list.html',
		{'acad_divs':acad_divs,
		'nums':nums})

	return render(request, 'labs/acad_div_list.html',
		{'acad_div_list':acad_div_list})


def show_lab(request, lab_id):
	lab = Lab.objects.get(pk=lab_id)
	return render(request, 'labs/lab.html',
		{'lab':lab})

def all_labs(request):
	# Setup pagination
	pag = Paginator(Lab.objects.all().order_by('name'), LABS_PER_PAGE)
	page =request.GET.get('page')
	labs = pag.get_page(page)
	nums = "a"*labs.paginator.num_pages

	return render(request, 'labs/lab_list.html',
		{'labs':labs,
		'nums':nums})


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

