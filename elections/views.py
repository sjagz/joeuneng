from django.shortcuts import render
from django.http import HttpResponse

def index(request):

	return render(request, 'elections/base.html')
	#return HttpResponse("hello world , joeuneng first , git changed finish , python anywhere django delelte")

def index01(request):

	return render(request, 'elections/Business field.html')