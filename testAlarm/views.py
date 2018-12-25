from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from testAlarm.models import DevID, Image
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404


def index(request):
    return render(request, "index.html")


def login_action(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            request.session['user'] = username
            response = HttpResponseRedirect("/devid_manage/")
            return response
        else:
            return render(request, "index.html", {'error': '用户名或密码错误!'})


@login_required
def devid_manage(request):
    devid_list = DevID.objects.all()
    username = request.session.get("user", '')
    return render(request, "devid_manage.html", {"user": username, "devids": devid_list})


@login_required
def image_list(request, eid):
    if not request.user.is_authenticated:
        images = get_object_or_404(Image, Aid=eid)
        return render(request, 'image_list.html', {'images': images})


@login_required
def logout(request):
    auth.logout(request)
    response = HttpResponseRedirect('/index/')
    return response


