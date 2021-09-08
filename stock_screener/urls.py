"""stock_screener URL Configuration

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
from momentum_app.views import Momentum2SP500, EpSP500, DetailSP500, Momentum2DJ30, EpDJ30, DetailDJ30, ListEtf, DetailEtf, ListDivs, ListNotes, UpdateNotes, Updatedj30, Updatesp500, Updatedivs, Updateetf 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('momentum/dj30/', Momentum2DJ30.as_view()),
    path('ep/dj30/', EpDJ30.as_view()),
    path('dj30/<symbol>', DetailDJ30.as_view()),
    path('momentum/sp500/', Momentum2SP500.as_view()),
    path('ep/sp500/', EpSP500.as_view()),
    path('etf/', ListEtf.as_view()),
    path('etf/<name>', DetailEtf.as_view()),
    path('divs/', ListDivs.as_view()),
    path('notes/', ListNotes.as_view()),
    path('notes/<id>', UpdateNotes.as_view()),
    path('update/dj30/', Updatedj30.as_view()),
    path('update/sp500/', Updatesp500.as_view()),
    path('update/divs/', Updatedivs.as_view()),
    path('update/etf/', Updateetf.as_view()),
]
