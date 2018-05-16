# -*- coding: UTF-8 -*-

from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.shortcuts import render
import datetime
from mysite.forms import ContactForm
from django.core.mail import send_mail,get_connection

# authentication example in "ch11-User Authentication in Django"
# 02- "Authentication in Web Requests
from django.contrib.auth import authenticate,login
from mysite.forms import LoginForm

# 实现 `logout_view` in "/authentication-web-requests/"
from django.contrib.auth import logout
from django.shortcuts import redirect

# 使用`login_required`装饰器
from django.contrib.auth.decorators import login_required

def home(request):
    if request.user.is_authenticated():
        # Do something for authenticated users.
        username = request.user.username
        email = request.user.email
        html = "<html><body>Welcome %s , your email in systme is  %s.</body></html>" % (username, email)
        return HttpResponse(html)
    else:
        # Do something for anonymous users.
        html = "<html><body>Welcome AnonymousUser to my sitle.</body></html>"
        return HttpResponse(html)

@login_required
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

def my_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = cd['username']
            password = cd['password']
            #username = request.POST['username']
            #password = request.POST['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    # Redirect to a success page.
                    #return HttpResponse("Login Successfully!")
                    #email = user.email
                    #html = "<html><body>Welcome %s , your email in systme is  %s.</body></html>" % (username, email)
                    #return HttpResponse(html)
                    return redirect('mhome')
                else:
                    # Return a 'disabled account' error message
                    return HttpResponse("Sorry, the user is a disabled account!")
            else:
                # Return a 'invalid login' error message
                return HttpResponse("Sorry, username or password is not correct!Please try it again!")
    else:
        form = LoginForm(
                # initial = {'subject':'I love your site!'}
                #initial = {'subject':'我喜欢你的网站！'}
                )
    return render(request,'login_form.html',{'form':form})

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect('mhome')
