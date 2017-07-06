# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from .models import VideoUpload,Category

def index(request):
	context = RequestContext(request) 
	video_list = VideoUpload.objects.all()
	cat = Category.objects.all()
	context_dict = {'Videos':video_list,'Categories':cat}
	return render_to_response('tube/index.html',context_dict,context)

	def __str__(self):
		return self.title

	def __str__(self):
		return self.description

def about(request):
	context = RequestContext(request)
	context_dict = {'boldmessage':"Its a bold message from rango"}
	return render_to_response('tube/about.html',context_dict,context)

def category_list(request):
	filter = CatFilter(request.GET,queryset = VideoUpload.objects.all())
	return render(request,'tube/category.html',{'filter':filter})


