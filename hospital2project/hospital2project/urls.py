"""hospital2project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import include,url
from hospital2app import views
urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$',views.home),
    url(r'^home/',views.home),
    url(r'^doctors/',views.doctors),
    url(r'^patients/',views.patients),
    url(r'^nurses/',views.nurses),
    url(r'^reports/',views.reports),
    url(r'^messages/',views.messages),
    url(r'^contact/',views.contact),
    url(r'^feedback/',views.feedback),
    url(r'^gellery/',views.gellery),
]
