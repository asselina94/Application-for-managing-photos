from django.shortcuts import render
from django.http import HttpResponse
import matplotlib.pyplot as plt
import requests
from colorthief import ColorThief
import matplotlib.pyplot as plt
import colorsys
import urllib
import os

# Create your views here.



def users(request):
    #pull data from third party rest api
    response = requests.get('https://jsonplaceholder.typicode.com/photos')
    #convert reponse data into json
    users = response.json()
    for user in users:
        st = (user['thumbnailUrl']).split("/")
        l = len(st)-1
        color = st[l]
        height,width =st[l-1],st[l-1]
        user['color'] = color
        user['height'] = height
        user['width'] = width
        
    return render(request, 'photos/users.html',{'users': users})
    #pass



def addPhoto(request):
    return render(request, 'photos/add.html')

def delPhoto(request):
    return render(request, 'photos/delete.html')
#def gallery(request):
	#return render(request, 'photos/gallery.html')


#def viewPhoto(request,pk):
	#return render(request, 'photos/photo.html')

#create or update
