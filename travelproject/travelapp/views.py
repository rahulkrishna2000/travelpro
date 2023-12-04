from django.shortcuts import render
from .models import place


def demo(request):
    obj = place.objects.all()

    return render(request,'index.html',{'result':obj})
# Create your views here.
