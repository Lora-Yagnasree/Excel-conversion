"""
URL configuration for excelproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
# urls.py
# excelproject/urls.py

from django.contrib import admin
from django.urls import path
from excelapp import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('applicants/', views.applicant_list, name='applicant_list'),
    path('export_excel/', views.export_applicants_to_excel, name='export_excel'),
]
