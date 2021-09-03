from django.urls import path
from .import views
urlpatterns=[ # it s always a good practice to  end a address with slash
    path('',views.home),
    path('register/',views.register,name='register'),
    path('login/',views.login_request,name='login_request'),
    path('logout/',views.logout_request,name='logout_request'),
    path('add/',views.add_item,name='add_item'),
    path('update/<str:pk>',views.update_item,name='update_item'),
    path('delete/<str:pk>',views.delete_item,name='delete_item'),
    path('filter/',views.filter_date,name='filter_date')
]