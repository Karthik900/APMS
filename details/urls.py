from django.urls import path, include
from rest_framework import routers

from . import views

app_name = 'details'

router = routers.DefaultRouter()
router.register('User', views.UserViewsSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('index/', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    # path('register/', views.register, name='register'),
    path('login/edit/', views.edit, name='edit'),
    path('login/home/', views.home, name='home'),
    path('login/contacts/', views.contacts, name='contacts'),
    path('login/events/', views.events, name='events'),
    path('login/gallery/', views.gallery, name='gallery'),
    path('login/association/', views.association, name='association'),
    path('login/profile/', views.profile, name='profile'),
]
