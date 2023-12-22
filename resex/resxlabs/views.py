from django.shortcuts import render
from django.core.paginator import Paginator
from labs.models import Lab, Academic_Division
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.
LABS_PER_PAGE = 10


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

@csrf_exempt
def all_labs(request):
	labs = Lab.objects.all().order_by('academic_division__name','name')

	if is_ajax(request) and request.method == 'POST':
		data = request.POST.get('lab_id')
		print(data)
		return JsonResponse({"message": "Data received successfully!"})
	
	# elif request.method == "POST":
	# 	searched_labs = request.POST.get('searched_labs')
	# 	if searched_labs != "":
	# 		labs = Lab.objects.filter(name__contains= searched_labs) | Lab.objects.filter(academic_division__name__contains= searched_labs) | Lab.objects.filter(description__contains=searched_labs)
	# 	else:
	# 		labs = Lab.objects.all().order_by('academic_division__name','name')
	# Setup pagination
	pag = Paginator(labs, LABS_PER_PAGE)
	page =request.GET.get('page')
	labs = pag.get_page(page)
	nums = "a"*labs.paginator.num_pages
	

	return render(request, 'resxlab/listing_labs.html',{'labs':labs,'nums':nums})