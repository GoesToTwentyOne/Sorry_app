from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('love/',views.love,name='love'),
    path('sorry1/',views.sorry_one,name='sorry1'),
    path('sorry2/',views.sorry_two,name='sorry2'),
    path('sorry3/',views.sorry_three,name='sorry3'),
    path('sorry4/',views.sorry_four,name='sorry4'),
    path('love2/',views.love_two,name='love2'),
   
]
