
from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('movies/', getMoviesIDs, name="moviesids"),
    path('tv_series/', getTvSeriesIds, name="tvseries"),
    path('people/', getPeopleIDs, name="peopleids"),
    path('production_companies/', getProductionCompaniesIDs, name ="productionCompanyids")

]
"""TODO
path('collection_ids/', admin.site.urls),
path('tv_network_ids/', admin.site.urls),
path('keyword_ids/', admin.site.urls),
"""