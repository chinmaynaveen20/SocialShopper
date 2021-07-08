"""socialShopper URL Configuration

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
import contactus.views as cviews
import accounts.views as aviews
import shoppings.views as sviews
urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', cviews.contact, name = "contact"),
    path('', aviews.home, name = "home"),
    path("login/", aviews.login, name = "login"),
    path('home/', sviews.user_home, name = "user_home"),
    path('home/<str:status>', sviews.user_home, name = "user_home"),
    path("logout/", aviews.logout, name = "logout"),
    path("shop/<int:shopping_id>", sviews.shopping_home, name = "shopping_detail")


]
