from django.contrib import admin
from django.conf.urls import url,include
from django.urls import path
from . import views

urlpatterns = [
	#url(r'^$', views.index),


	path('first/', views.index),
    #path('result/', admin.site.urls),
]
