"""Thief_Detection URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path('', views.log),
     path('log_post', views.log_post),
     path('admin_home', views.admin_home),
     path('police_add', views.police_add),
     path('police_add_post', views.police_add_post),
     path('view_police', views.view_police),
     path('update_police/<id>', views.update_police),
     path('update_police_post/<id>', views.update_police_post),
     path('delete_police/<id>', views.delete_police),
     path('add_criminal_category', views.add_criminal_category),
     path('add_criminal_category_post', views.add_criminal_category_post),
     path('view_category', views.view_category),
     path('delete_category/<id>', views.delete_category),
     path('view_detection_details', views.view_detection_details),
     path('view_criminals', views.view_criminals),
     path('view_user', views.view_user),
     path('logout', views.logout),

######################################################################################
     path('police_home',views.police_home),
     path('view_profile',views.view_profile),
     path('add_criminal',views.add_criminal),
     path('add_criminal_post',views.add_criminal_post),
     path('view_criminal',views.view_criminal),
     path('update_criminal/<id>',views.update_criminal),
     path('update_criminal_post/<id>',views.update_criminal_post),
     path('delete_criminal/<id>',views.delete_criminal),
     path('view_users',views.view_users),
     path('view_crminal_alert',views.view_crminal_alert),

##############################################################################
     path('android_login',views.android_login),
     path('android_user_registration',views.android_user_registration),
     path('android_view_profile',views.android_view_profile),
     path('android_view_visitorlog',views.android_view_visitorlog),
     path('android_view_femiliarlog',views.android_view_femiliarlog),
     path('android_view_criminal',views.android_view_criminal),
     path('android_add_familiar_person',views.android_add_familiar_person),
     path('android_view_familiar_person',views.android_view_familiar_person),
     path('android_delete_familiar_person',views.android_delete_familiar_person),
     path('android_add_camera',views.android_add_camera),
     path('android_view_camera',views.android_view_camera),
     path('android_delete_camera',views.android_delete_camera),
     path('android_update_familiar_persons',views.android_update_familiar_persons),
     path('android_update_familiar_person',views.android_update_familiar_person),


]
