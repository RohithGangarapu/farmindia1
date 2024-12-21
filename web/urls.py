from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name="home"),
    path('login',views.login,name="login"),
    path('sell',views.sell,name="sell"),
    path('producer',views.producer,name="producer"),
    path('consumer',views.consumer,name="consumer"),
    path('sellfruits',views.sellfruits,name="sellfruits"),
    path('sellveg',views.sellveg,name="sellveg"),
    path('sellcrop',views.sellcrop,name="sellcrop"),
    path('sellinfo',views.sellinfo,name="sellinfo"),
    path('buyfruits',views.buyfruits,name="buyfruits"),
    path('buyveg',views.buyveg,name="buyveg"),
    path('buycrop',views.buycrop,name="buycrop"),
]