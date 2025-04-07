from django.urls import path
from .views import AnimeToSwipeView,SwipeAPIView
from . import views

urlpatterns=[
    path('swipe/',views.swipe_page, name='swipe-page'),
    path('swipe/anime/',AnimeToSwipeView.as_view(),name='anime-to-swipe'),
    path('swipe/',SwipeAPIView.as_view(),name='swipe-anime')
]