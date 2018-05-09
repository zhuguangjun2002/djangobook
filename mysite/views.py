from django.http import HttpResponse
from django.shortcuts import render
import datetime


def hello(request):
    return HttpResponse("Hello world") 

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request,"current_datetime.html",{'current_date':now})

def hours_ahead(request,offset):
    try:
        offset = int(offset)
    except:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    #assert False
    html = "<html><body>In %s hour(s), it will be  %s.</body></html>" % (offset, dt)
    return HttpResponse(html)
