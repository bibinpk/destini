from django.shortcuts import render
from destination.models import destination, popular, districts


# Create your views here.

def index(request):
    dist = districts.objects.get(name="IDUKKI")
    pops = popular.objects.all()
    return render(request, 'index.html', {'pops': pops, 'dist': dist})


def destinations(request, district):
    dist_id = districts.objects.get(name=district)
    dist = districts.objects.all()
    dest = destination.objects.filter(district=dist_id)
    return render(request, 'destinations.html', {'dists': dist, 'dests': dest})


def destination_details(request, dest_name):
    dist = districts.objects.get(name="IDUKKI")
    dest = destination.objects.get(name=dest_name)
    return render(request, "destination_details.html", {'dest': dest, 'dist': dist})


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")
