from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
# Create your views here.

from .models import URLMapping

from django.forms.models import model_to_dict

def get_all(request):
	url_mappings = URLMapping.objects.all()
	response = []
	for url_map in url_mappings:
		response.append(model_to_dict(url_map))
	return JsonResponse(response, safe=False)

def redirect(request, short):
	response = None
	url_map = URLMapping.objects.filter(short_link=short).first()

	print(url_map)

	if not url_map:
		response = {
			"error": "Not Found"
		}

		return JsonResponse(response)
	else:
		response = {
			"original_link": url_map.original_link
		}

		url_map.count += 1
		url_map.save()

		return HttpResponseRedirect(url_map.original_link)
