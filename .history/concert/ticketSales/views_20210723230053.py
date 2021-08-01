from django.shortcuts import render
from django.http import HttpResponse
from ticketSales.models import concertModel

# Create your views here.

def concertListView(request):
    return HttpResponse("لیست کنسرت های موجود")