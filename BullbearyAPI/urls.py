"""BullbearyAPI URL Configuration

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
from django.urls import path
from django.conf.urls import url, include 
#from users.views import GoogleLogin
from rest_framework_simplejwt import views as jwt_views
from django.contrib import admin
from users.views import FacebookLogin, FacebookConnect, GoogleLogin, GoogleConnect
from dj_rest_auth.registration.views import SocialAccountListView, SocialAccountDisconnectView
from posts.views import PostList, PostDetail
from comments.views import CommentList, CommentDetail
from tags.views import TagList, TagDetail

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('', include('stocks.urls')),
    path('api/', include('dj_rest_auth.urls')),
    path('api/accounts/', include('allauth.urls'), name='socialaccount_signup'),
    path('api/accounts/registration/', include('dj_rest_auth.registration.urls')),
    path('api/accounts/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('api/accounts/facebook/connect/', FacebookConnect.as_view(), name='fb_connect'),
    path('api/accounts/google/', GoogleLogin.as_view(), name='gl_login'),
    path('api/accounts/google/connect/', GoogleConnect.as_view(), name='gl_connect'),
    path('api/accounts/socialaccounts/', SocialAccountListView.as_view(), name='social_account_list'),
    path('api/accounts/socialaccounts/<int:pk>/disconnect/', SocialAccountDisconnectView.as_view(), name='social_account_disconnect'),
    path('posts/', PostDetail.as_view()),
    path('posts/<int:pk>/', PostDetail.as_view()),
    path('comments/', CommentList.as_view()),
    path('comments/<int:pk>/', CommentDetail.as_view()),
    path('tags/', TagList.as_view()),
    path('tags/<int:pk>/', TagDetail.as_view()),
]