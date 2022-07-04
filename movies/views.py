import json 

from django.http import JsonResponse, HttpResponse
from django.views import View 
from django.core.exceptions import ObjectDoesNotExist

from owners.models import Owner, Dog 

class ActorsView(View):
    pass

class MoviesView(View):
    pass