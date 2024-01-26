from django.urls import path, include
from watchlist_app.api.views import (
    StreamPlatformAV,
    WatchListAV,
    WatchListDetailsAV,
    StreamPlatformDetailAV,
    ReviewList,
    ReviewDetail,
)

urlpatterns = [
    path("list/", WatchListAV.as_view(), name="watchlist"),
    path("<int:pk>", WatchListDetailsAV.as_view(), name="watchlist-details"),
    path("stream/", StreamPlatformAV.as_view(), name="stream"),
    path("stream/<int:pk>", StreamPlatformDetailAV.as_view(), name="stream-details"),
    path(
        "stream/<int:pk>/review",
        ReviewList.as_view(),
        name="review-details",
    ),
    path("stream/review/<int:pk>", ReviewDetail.as_view(), name="review-details"),
]
