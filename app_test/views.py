# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
# from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import reverse


def index(request):
    # return HttpResponse(u'欢迎光临 王爷的项目')
    # return render(request, 'app_test/home.html')
    string = u'我在学习django'
    TutorialList = [u"HTML", "CSS", "jQuery", "Python", "Django"]
    info_dict = {'site': u'haha', 'content': u'这里是内容'}
    List = map(str, range(100))
    athlete = []
    res_dict = {
        'string': string,
        'TutorialList': TutorialList,
        'info_dict': info_dict,
        'List': List,
        'athlete': athlete
    }
    return render(request, 'app_test/home.html', res_dict)

# def home(request):
#     string = u'我在学习django'
#     return render(request, 'app_test/home.html', {'string': string})


def add(request):
    a = request.GET['a']  # a = request.GET.get('a', 0)
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))


def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))


def old_add2_redirect(request, a, b):
    return HttpResponseRedirect(
        reverse('add2', args=(a, b))
    )


def add3(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))













