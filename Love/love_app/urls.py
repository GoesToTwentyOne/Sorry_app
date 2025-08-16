from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('love/',views.love,name='love'),
    path('love2/',views.love_two,name='love2'),
]
