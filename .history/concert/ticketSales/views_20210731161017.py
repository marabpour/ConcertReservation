from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from ticketSales.models import concertModel
from ticketSales.models import locationModel
from ticketSales.models import timeModel
import accounts
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from ticketSales.forms import SearchForm

# Create your views here.

def concertListView(request):
    
    searchForm=SearchForm(request.GET)
    if searchForm.is_valid():
        SearchText=searchForm.cleaned_date["SearchText"]
        
    concerts=concertModel.objects.all()
    
    context={
        
        "concertlist":concerts,
        "concertcount":concerts.count(),
        "searchForm":searchForm
    }
    return render(request,"ticketSales/concertlist.html",context)

@login_required
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


@login_required
def timeView(request):

    # if request.user.is_authenticated  and request.user.is_active:

        times=timeModel.objects.all()

        context={

            "timelist":times,
        }

        return render(request,"ticketSales/timeList.html",context)
    # else:
    #     return HttpResponseRedirect(reverse(accounts.views.loginView))
        
    