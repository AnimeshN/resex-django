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
		lab_id = request.POST.get('lab_id')
		lab = Lab.objects.get(pk=lab_id)
		acad_div = Academic_Division.objects.get(pk=lab.academic_division.id)
		image_url = lab.lab_image.url

		lab_data = {
            'name': lab.name,
            'academic_division': acad_div.name,
            'faculty': lab.faculty,
            'contact': lab.contact,
            'description': lab.description,
            'web': lab.web,
            'email_address': lab.email_address,
            'address': lab.address,
            'poc_manager': lab.poc_manager.username,
            'poc_manager_email': lab.poc_manager.email,
            'lab_image': image_url,
            'research_equipment': lab.research_equipment,
        }
		print(lab_data)
		return JsonResponse(lab_data)
	
	elif request.method == "POST":
		searched_labs = request.POST.get('searched_labs')
		if searched_labs != "":
			labs = Lab.objects.filter(name__contains= searched_labs) | Lab.objects.filter(academic_division__name__contains= searched_labs) | Lab.objects.filter(description__contains=searched_labs)
		else:
			labs = Lab.objects.all().order_by('academic_division__name','name')
	# Setup pagination
	pag = Paginator(labs, LABS_PER_PAGE)
	page =request.GET.get('page')
	labs = pag.get_page(page)
	nums = "a"*labs.paginator.num_pages
	

	return render(request, 'resxlab/listing_labs.html',{'labs':labs,'nums':nums})