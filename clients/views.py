from django.shortcuts import render,redirect
from .models import Client
from .forms import ClientForm #create this next
# Create your views here.
def add_client(request):
    if request.method=='POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add-client')
        
    else:
        form = ClientForm()
    return render(request, 'clients/add_client.html', {'form':form})   
# Create your views here.
