from django.urls import path, include
from rest_framework.routers import DefaultRouter
from watchlist_app.api.views import WatchListAV, WatchDetailAV, StreamPlatformAV, StreamPlatformDetailAV, ReviewList, ReviewDetail, ReviewCreate, StreamPlatformViewSet

router = DefaultRouter()
router.register('stream-vs', StreamPlatformViewSet, basename='stream-vs')

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie_list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie_details'),
    path('stream/', StreamPlatformAV.as_view(), name='stream'),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream_details'),
    path('<int:pk>/reviews/', ReviewList.as_view(), name='review_list'),
    path('<int:pk>/review_create/',
         ReviewCreate.as_view(), name='review_create'),
    path('review/<int:pk>', ReviewDetail.as_view(), name='review_details'),
    path('', include(router.urls)),
    path('api-auth/', include("rest_framework.urls")),
]
