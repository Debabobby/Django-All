# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 09:51:48 2021

@author: Bobby
"""

from django.urls import path
from . import views


urlpatterns=[
    path('',views.home,name='Home'),
    path('projects/<str:pk>',views.projects,name="project"),
    
    ]