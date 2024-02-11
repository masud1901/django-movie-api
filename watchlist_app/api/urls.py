from django.urls import path, include
from watchlist_app.api.views import (
    # StreamPlatformAV,
    WatchListAV,
    WatchListDetailsAV,
    # StreamPlatformDetailAV,
    StreamPlatformVS,
    ReviewList,
    ReviewDetail,
    ReviewCreate,
    WatchListVS
)

from rest_framework import routers

router = routers.DefaultRouter()
router.register("stream", StreamPlatformVS, basename="stream-platform")
router.register("list", WatchListVS, basename="watch-list")


urlpatterns = [
    path("", include(router.urls)),
    # path("list/", WatchListAV.as_view(), name="watchlist"),
    # path("<int:pk>/", WatchListDetailsAV.as_view(), name="watchlist-details"),
    path("<int:pk>/review-create/", ReviewCreate.as_view(), name="review-create"),
    path(
        "<int:pk>/review/",
        ReviewList.as_view(),
        name="review-details",
    ),
    path("review/<int:pk>/", ReviewDetail.as_view(), name="review-details"),
]
