"""textcount URL Configuration
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

from django.urls import path
# . == this directory
from . import views


urlpatterns = [
    # create views.py to send back information
    # if someone doesn't give us anything ('') after the homepage, we want to send them to views.home
    path('', views.home, name='home'),
    # best practice to put trailing slash at the end of path
    # need to reference name given in our form action
    path('count/', views.count, name='count'),
    path('about/', views.about, name='about')
]