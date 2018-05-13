# -*- coding: UTF-8 -*-

from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.shortcuts import render
import datetime
from mysite.forms import ContactForm
from django.core.mail import send_mail,get_connection

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

def display_meta(request):
    values = request.META
    html = []
    for k in sorted(values):
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, values[k]))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(
                    cd['subject'],
                    cd['message'],
                    cd.get('email','noreply@example.com'),
                    ['siteowner@example.com'],
                    connection = con
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
                # initial = {'subject':'I love your site!'}
                initial = {'subject':'我喜欢你的网站！'}
                )
    return render(request,'contact_form.html',{'form':form})

def contact_thanks(request):
    html = "Thanks!"
    return HttpResponse(html)
