from __future__ import unicode_literals
from django.shortcuts import render
from . import models
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.views import generic
from . import forms
def music(request):
	if request.user.is_authenticated:
		movies=models.movielist.objects.all()
		return render(request,'musico/home.html',{'movielist':movies})
	else:
		return HttpResponse("you need access to access the list")
def listsong(request,pk):
	if request.user.is_authenticated:
		movies=models.movielist.objects.get(pk=pk)
		return render(request,'musico/list.html',{'album':movie})
	else:
		return HttpResponse('You need to login to get access song')
def add_movie(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.MovieForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponse("movie saved")
        else:
            form = forms.MovieForm()
        return render(request, 'musico/setting.html', {'form': form})
    else:
        return HttpResponse("you need to login to access song")

def add_song(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.SongForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponse("song saved")
        else:
            form = forms.SongForm()
        return render(request, 'musico/songsave.html', {'form': form})
    else:
        return HttpResponse("you need to login to access song")
