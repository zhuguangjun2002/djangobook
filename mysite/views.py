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

# 使用`user_passes_test`装饰器
from django.contrib.auth.decorators import user_passes_test

# 使用自定义的`SignUpForm`,创建`signup`视图
from mysite.forms import SignUpForm

# 使用csv
import csv

# 使用 streaming response
from django.utils.six.moves import range
from django.http import StreamingHttpResponse

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

def email_check(user):
    if user.is_authenticated():
        if user.email:
          return user.email.endswith('@163.com')
        else:
          return False
    else:
        return False

#@user_passes_test(email_check, login_url='login')
@user_passes_test(email_check)
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

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=raw_password)
            login(request,user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request,'signup.html',{'form':form})

def my_image(request):
    image_data =  open("/home/user/project/djangobook/mysite_project/mysite/images/dc-3.png", "rb").read()
    return HttpResponse(image_data, content_type="image/png")

# 显示csv文件
def my_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename="dc-3-airplane.csv"'
    writer = csv.writer(response)
    writer.writerow(['Role','Airliner and transport aircraft'])
    writer.writerow(['National origin','United States'])
    writer.writerow(['Manufacturer','Douglas Aircraft Company'])
    writer.writerow(['First flight','December 17, 1935'])
    writer.writerow(['Introduction','1936'])
    writer.writerow(['Status','In service'])
    writer.writerow(['Produced','1936–1942, 1950'])
    writer.writerow(['Number built','607'])
    writer.writerow(['Unit cost','US$79,500 (equivalent to $1,419,036 in 2017)'])
    writer.writerow(['Developed from','Douglas DC-2'])
    writer.writerow(['Variants','Douglas C-47 Skytrain','Lisunov Li-2','Showa/Nakajima L2D','Basler BT-67','Conroy Turbo Three','Conroy Tri-Turbo-Three'])
    return response


class Echo(object):
    """An object that implements just the write method of the file-like
    interface.
    """
    def write(self, value):
        """Write the value by returning it, instead of storing in a buffer."""
        return value

def my_streaming_csv_view(request):
    """A view that streams a large CSV file."""
    # Generate a sequence of rows. The range is based on the maximum number of
    # rows that can be handled by a single sheet in most spreadsheet
    # applications.
    rows = (["Row {}".format(idx), str(idx)] for idx in range(65536))
    pseudo_buffer = Echo()
    writer = csv.writer(pseudo_buffer)
    response = StreamingHttpResponse((writer.writerow(row)
      for row in rows), content_type="text/csv")
    response['Content-Disposition'] = 'attachment;filename="somefilename.csv"'
    return response
