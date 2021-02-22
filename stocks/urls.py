from django.conf.urls import url 
from django.urls import path
from stocks import views 
 
urlpatterns = [ 
    path('api/stocks', views.stock_list)
]