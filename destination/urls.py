from django.urls import path

import destini
from destination.views import index, destinations, destination_details, about, contact

urlpatterns = [
    path('', index),
    path('destinations/<str:district>/', destinations),
    path('destination/<str:dest_name>/', destination_details),
    path('about/', about),
    path('contact/', contact),

]