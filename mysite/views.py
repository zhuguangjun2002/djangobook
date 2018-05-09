#from django.template import Template, Context
from django.template.loader import get_template
from django.http import HttpResponse
import datetime


def hello(request):
    return HttpResponse("Hello world") 

def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template("current_datetime.html")
    #t = Template("<html><body>It is now {{ current_date }}.</body></html>")
    #html = t.render(Context({'current_date':now}))
    html = t.render({'current_date':now})
    return HttpResponse(html)

def hours_ahead(request,offset):
    try:
        offset = int(offset)
    except:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    #assert False
    html = "<html><body>In %s hour(s), it will be  %s.</body></html>" % (offset, dt)
    return HttpResponse(html)
