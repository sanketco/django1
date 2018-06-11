from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from . import models
# Create your views here.
def movie(request):
	   return HttpResponse(" tmovies will be displayed here")

class list(ListView):
	model = models.movielist
	context_object_name = 'movie_list'
	template_name = 'movie/sample.html'
class list(ListView):
	model = models.song
	context_object_name = 'movie_list'
	template_name = 'movie/sample.html'
def detail(request,pk):
	movie = models.movielist.objects.get(pk=pk)
	return render(request,'movie/detailview.html',{'movie':movie})