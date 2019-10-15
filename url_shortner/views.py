from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

from .models import URLMapping

from django.forms.models import model_to_dict

def get_all(request):
	url_mappings = URLMapping.objects.all()
	response = []
	for url_map in url_mappings:
		response.append(model_to_dict(url_map))
	return JsonResponse(response, safe=False)