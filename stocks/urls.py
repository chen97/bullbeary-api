from django.conf.urls import url
from django.urls import path
from stocks import views

urlpatterns = [
    path('', views.myResponse),
    path('<int:stock_code>', views.get_details)
]
