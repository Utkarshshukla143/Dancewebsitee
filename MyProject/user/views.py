from django.db import connection
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import datetime


# Create your views here.
def home(req):
    cdata = category.objects.all().order_by('-id')[0:6]

    return render(req, 'user/index.html', {"data": cdata, })


def about(req):
    return render(req, 'user/about.html')


def contactus(request):
    status = False
    if request.method == "POST":
        a = request.POST.get("name", "")
        b = request.POST.get("mobile", "")
        c = request.POST.get("email", "")
        d = request.POST.get("msg", "")
        x = contact(name=a, email=b, contact=c, message=d)
        x.save()
        status = True
    # u return HttpResponse("<script>alert('Thanks For Enquiry');window.location.href='/user/contactus/'</script>")
    return render(request, 'user/contactus.html', {'S': status})


def myblogs(request):
    if request.session.get('user'):
        id=request.session.get('user')
        blogdata=blogdetail.objects.filter(authorid=id).order_by('-blogdate')
        return render(request,'user/myblogs.html',{"bdata":blogdata})
    else:
        return HttpResponse("<script>alert('Please login first to see blog list3-....');window.location.href='/user/signin/';</script>")


def createblogs(req):
    if req.session.get('user'):
        cdata = category.objects.all()
        if req.method == 'POST':
            authorid = req.session.get('user', " ")
            bcategory = req.POST.get('blogcategory', " ")
            title = req.POST.get('title', " ")
            bdesc = req.POST.get('discription', "")
            attachment = req.POST.get('attachment')
            thumbnail = req.POST.get('thumbnail')
            data = blogdetail(authorid=authorid, blogcategory=bcategory, title=title, description=bdesc,
                              attechment=attachment, thumbnail=thumbnail, blogdate=datetime.datetime.now())
            data.save()
        return render(req, 'user/createblogs.html', {"category": cdata})
    else:
        return HttpResponse("<script>alert('Please login firstvto add blogs....');window.location.href='/user/signin/';</script>")


def latestblogs(req):
    cursor = connection.cursor()
    if (req.GET.get('id') is None):
        cursor.execute(
            "select b.*,u.* from user_blogdetail b , user_profile u where b.authorid=u.email order by b.blogdate desc")
    else:
        id = req.GET.get('id')
        cursor.execute(
            "select b.*,u.* from user_blogdetail b , user_profile u where b.authorid=u.email and b.blogcategory='" + id + "' order by b.blogdate desc")
    bdetail = cursor.fetchall()
    print(bdetail)
    cdata = category.objects.all().order_by('-id')
    return render(req, 'user/latestblogs.html', {"bdetail": bdetail, "data": cdata})

def about(req):
    return render(req, 'user/about.html')


def signup(req):
    if req.method == 'POST':
        name = req.POST.get("name", "")
        email = req.POST.get("email", "")
        mobile = req.POST.get("mobile", "")
        password = req.POST.get("passwd", "")
        address = req.POST.get("address", "")
        picname = req.FILES['fu']
        profile(name=name, mobile=mobile, email=email, passwd=password, address=address, ppic=picname).save()
        return HttpResponse("<script>alert('You are registerded successfully..');window.location.href='/user/signup/';</script>")
    return render(req, 'user/signup.html')

def signin(request):
    if request.method == 'POST':
        uname = request.POST.get('uname', "")
        passwd = request.POST.get('passwd', "")
        checkuser = profile.objects.filter(email=uname, passwd=passwd)
        if (checkuser):
            request.session['user'] =uname
            return HttpResponse("<script>alert('LoggedIn Successfully');window.location.href='/user/signin';</script>")
        else:
            return HttpResponse("<script>alert('UserId or password is incorrect');window.location.href='/user/signin';</script>")
    return render(request, 'user/signin.html')

def logout(request):
    del request.session['user']
    return HttpResponse("<script>window.location.href='/user/home/';</script>")

def myprofile(request):
    if request.session.get('user'):
        id=request.session.get('user')
        userdata=profile.objects.filter(email=id)[0:1]
        return render(request,'user/myprofile.html',{'userdata':userdata})
    else:
        return HttpResponse("<script>alert('Please login first to see your profile');window.location.href='/user/signin';</script>")
