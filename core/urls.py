from django.urls import path
from . import views
from core.views import AnimeToSwipeView,SwipeAPIView
urlpatterns = [
    path('swipe/', views.swipe_page, name='swipe-page'),
    path('swipe/anime/', AnimeToSwipeView.as_view(), name='anime-to-swipe'),
    path('swipe/action/', SwipeAPIView.as_view(), name='swipe-anime'),
]