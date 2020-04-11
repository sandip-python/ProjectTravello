from django.shortcuts import render
from . models import Destiny

# Create your views here.
def index(request):
    dests = Destiny.objects.all()
    return render(request, 'index.html', {'dests': dests})