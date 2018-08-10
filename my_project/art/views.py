from django.shortcuts import render
from django.http import HttpResponse
from art.models import company
import datetime
# Create your views here.

def app(request):
    l = ['Icecream', 'Burgger', 'Cooldrink']
    myName = 'Arun Nettyam'
    t = datetime.datetime.now()
    get_company = company.objects.all()
    arg={'name': myName, 'food': get_company, 'date': t}
    return render(request, 'Art/Forms.html', arg)

def submit(request):
    return render(request, 'Art/submit.html')
