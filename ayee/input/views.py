from django.shortcuts import render
from django.http import Http404

# Create your views here.
def home(request):
	return render(request, 'ayee/home.html')
	
def subproject(request):
	return render(request, 'ayee/subproject.html')
	
