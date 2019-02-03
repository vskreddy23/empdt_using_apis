"""empdt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url,patterns
from django.contrib import admin
from crud import views
from crud.models import Empdtls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.AboutView.as_view()),
    url(r'^loginview/',views.LoginView.as_view()),
    url(r'^empdetails/',views.crudListView.as_view(),name= 'crud_List'),
    url(r'^viewdetails/(?P<pk>[-\d]+)/', views.crudDetailView.as_view(),name='emp_Details'),
    url(r'^crud/Empdtls-add/',views.EmpdtlsCreate.as_view(),name = 'Empdtls-add'),
    url(r'^edit/(?P<pk>[-\d]+)/', views.EmpdtlsUpdate.as_view(), name= 'Empdtls-edit'),
    url(r'^delete/(?P<pk>\d+)/', views.EmpdtlsDelete.as_view(), name='Empdtls-delete'),
    url(r'^recent/', views.EmpdtlsList.as_view(), name= 'Empdtls-recent'),
    url(r'^logout/',views.LogoutView.as_view()),
]