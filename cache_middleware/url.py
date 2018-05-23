
from django.contrib import admin
from django.urls import path
urlpatterns = [
    path('movie_ids/', admin.site.urls),
    path('tv_series_ids/', admin.site.urls),
    path('person_ids/', admin.site.urls),
    path('collection_ids/', admin.site.urls),
    path('tv_network_ids/', admin.site.urls),
    path('keyword_ids/', admin.site.urls),
    path('production_company_ids/', admin.site.urls)
]