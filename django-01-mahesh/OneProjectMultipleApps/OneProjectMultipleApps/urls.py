"""
URL configuration for OneProjectMultipleApps project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from firstapp import views as v1
from secondapp import views as v2
from firstapp.views import wish1
from secondapp.views import wish2
urlpatterns = [
    path('admin/', admin.site.urls),
    path('wish1/',v1.wish1),
    # path('wish2/',v2.wish2),
    path('wish2/', wish2)
    
]
