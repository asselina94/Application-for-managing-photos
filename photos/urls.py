from django.urls import path
from . import views


urlpatterns = [
	
	path('', views.users, name = 'users'),
	path('add/',views.addPhoto, name = 'add'),
	path('del/',views.delPhoto, name = 'del'),
	#path('',views.gallery, name = 'gallery'),
	#path('photo/<str:pk>/',views.viewPhoto, name = 'photo'),


]