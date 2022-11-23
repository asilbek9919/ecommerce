from app.views import Home, ProfileList,ProfileCrete,Watch,ShowMovieDeatil,ShowMove
from django.urls import path


app_name='app'

urlpatterns = [
    path('', Home.as_view(), name='Home'),
    path('profile/',ProfileList.as_view(),name='profile_list'),
    path('profile/create/',ProfileCrete.as_view(),name='profile_create'),
    path('watch/<str:profile_id>/',Watch.as_view(),name='watch'),
    path('movie/detail/<str:movie_id>/',ShowMovieDeatil.as_view(),name='show_det'),
    path('movie/<str:movie_id>/',ShowMove.as_view(),name='play'),
    
]















