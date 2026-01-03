from django.shortcuts import render,get_object_or_404
from .models import ChaiVariety

# Create your views here.
def home(request):
    chais=ChaiVariety.objects.all()
    return render(request,'myapp\index.html',{'chais':chais})

def Description(request,chai_id):
    des=get_object_or_404(ChaiVariety,pk=chai_id)
    return render(request,'myapp\description.html',{'des':des})