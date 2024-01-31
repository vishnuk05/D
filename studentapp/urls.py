from django.urls import path
from .import views

urlpatterns=[
    path('',views.home, name='home'),
    path('view/',views.view, name='view'),
    path('delete/<str:pk>',views.delete, name='delete'),
    path('userlogout/', views.userlogout, name='userlogout'),
    path('validate/', views.validate, name='validate'),
    path('welcome/', views.welcome, name='welcome'),
    path('login/', views.login, name='login'),
    path('update/<int:pk>', views.update, name='update'),
    path('updateuser/', views.udpateuser, name='updateuser')
]