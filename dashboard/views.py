from django.shortcuts import render
from clients.models import Client
from loans.models import Loan

def dashboard(request):
    clients = Client.objects.count()
    loans= Loan.objects.count()
    return render(request,'dashboard.html',{
        'clients':clients,
        'loans':loans
    })