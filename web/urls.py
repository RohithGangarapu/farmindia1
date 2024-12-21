from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name="home"),
    path('login',views.login,name="login"),
    path('sell',views.sell,name="sell"),
    path('sellfruits',views.sellfruits,name="sellfruits"),
    path('sellveg',views.sellveg,name="sellveg"),
    path('sellcrop',views.sellcrop,name="sellcrop"),
]