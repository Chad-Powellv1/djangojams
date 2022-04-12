from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def index(request):
    return HttpResponse("some response here")

def albums(request):
    song = Song.objects.all().values()
    data = song
    return JsonResponse(data)

