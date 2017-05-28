# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

from .models import Course 

# Create your views here.
def all_courses(request):
  courses = Course.objects.all()
  return render(request, 'courses/all_courses.html', { 'courses': courses })