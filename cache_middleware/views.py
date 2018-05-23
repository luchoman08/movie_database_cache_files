from django.shortcuts import render
from .lib import *
from django.http import JsonResponse

# Create your views here.


def getMoviesIDs(request):
    return JsonResponse(getJsonMoviesIds(), safe=False)
def getPeopleIDs(request):
    return JsonResponse(getJsonPeopleIds(), safe=False)
def getTvSeriesIds(request):
    return JsonResponse(getJsonTvSeriesIds(), safe=False)
def getProductionCompaniesIDs(request):
    return JsonResponse(getJsonProductionCompanies(), safe=False)