from django.shortcuts import render
from django.http import HttpResponse
from ticketSales.models import concertModel
from ticketSales.models import locationModel
from ticketSales.models import timeModel

# Create your views here.

def concertListView(request):
    concerts=concertModel.objects.all()
    
    context={
        
        "concertlist":concerts,
        "concertcount":concerts.count()
    }
    return render(request,"ticketSales/concertlist.html",context)

def locationListView(request):
    locations=locationModel.objects.all()
    
    context={
        
        "locationlist":locations,
        
    }
    return render(request,"ticketSales/locationlist.html",context)

def concertDetailsView(request,concert_id):
    concert=concertModel.objects.get(pk=concert_id)

    context={
        "concertdetails":concert
    }

    return render(request,"ticketSales/concertDetails.html",context)