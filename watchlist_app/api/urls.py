from django.urls import path, include
from watchlist_app.api.views import StreamPlatformAV, WatchListAV, WatchListDetailsAV,StreamPlatformDetailAV

urlpatterns = [
    path("list/", WatchListAV.as_view(), name="watchlist"),
    path("<int:pk>", WatchListDetailsAV.as_view(), name="watchlist-details"),
    path("stream/", StreamPlatformAV.as_view(), name="stream"),
    path("stream/<int:pk>", StreamPlatformDetailAV.as_view(), name="stream-details"),
]
