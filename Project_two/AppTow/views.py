from django.shortcuts import render
from django.http import HttpResponse
from AppTow.models import Webpage,AccessRecord
# Create your views here.

def index(request):
   # my_dict = {"insert_me":"Hello I am from views.py!"}
  #  return render(request, 'AppTow/index.html',context=my_dict)

    Webpages= Webpage.objects.all()
    AccessRecords=AccessRecord.objects.all()
    
    my_present = {'Webpages':Webpages,'AccessRecords':AccessRecords}
    return render(request,'AppTow/index.html',my_present)    


