from watchlist_app.models import WatchList, StreamPlatform, Review
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import generics
from django.http import JsonResponse
from watchlist_app.api.serializers import (
    WatchListSerializer,
    StreamPlatformSerializer,
    ReviewSerializer,
)
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import viewsets


class WatchListAV(generics.ListCreateAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer


class WatchListDetailsAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer


# class WatchListAV(APIView):
#     def get(self, request):
#         watchlist = WatchList.objects.all()
#         serializer = WatchListSerializer(watchlist, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = WatchListSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# class WatchListDetailsAV(APIView):
#     def get(self, request, pk):
#         try:
#             content = WatchList.objects.get(pk=pk)
#         except WatchList.DoesNotExist:
#             return Response(
#                 {"Error": "The content is not listed!"},
#                 status=status.HTTP_404_NOT_FOUND,
#             )
#         serializer = WatchListSerializer(content)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def put(self, request, pk):
#         try:
#             content = WatchList.objects.get(pk=pk)
#         except WatchList.DoesNotExist:
#             return Response(
#                 {"Error": "The content is not listed!"},
#                 status=status.HTTP_404_NOT_FOUND,
#             )
#         serializer = WatchListSerializer(content, data=request.data, partial=True)
#         if not serializer.is_valid():
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def delete(self, request, pk):
#         try:
#             content = WatchList.objects.get(pk=pk)
#         except WatchList.DoesNotExist:
#             return Response(
#                 {"Error": "The content is not listed!"},
#                 status=status.HTTP_404_NOT_FOUND,
#             )
#         content.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class StreamPlatformVS(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer



# class StreamPlatformAV(APIView):
#     def get(self, request):
#         platform = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(platform, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = StreamPlatformSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# class StreamPlatformDetailAV(APIView):
#     def get(self, request, pk):
#         try:
#             content = StreamPlatform.objects.get(pk=pk)
#         except StreamPlatform.DoesNotExist:
#             return Response(
#                 {"Error": "The stream platform is not listed!"},
#                 status=status.HTTP_404_NOT_FOUND,
#             )
#         serializer = StreamPlatformSerializer(content)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def put(self, request, pk):
#         try:
#             content = StreamPlatform.objects.get(pk=pk)
#         except StreamPlatform.DoesNotExist:
#             return Response(
#                 {"Error": "The stream platform is not listed!"},
#                 status=status.HTTP_404_NOT_FOUND,
#             )
#         serializer = StreamPlatformSerializer(content, data=request.data, partial=True)
#         if not serializer.is_valid():
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def delete(self, request, pk):
#         try:
#             content = StreamPlatform.objects.get(pk=pk)
#         except StreamPlatform.DoesNotExist:
#             return Response(
#                 {"Error": "The stream platform is not listed!"},
#                 status=status.HTTP_404_NOT_FOUND,
#             )
#         content.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class ReviewList(mixins.ListModelMixin, generics.GenericAPIView):
    # queryset = Review.objects.all()
    def get_queryset(self):
        pk = self.kwargs["pk"]
        return Review.objects.filter(watchlist=pk)

    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        pk = self.kwargs.get("pk")
        watchlist = WatchList.objects.get(pk=pk)
        serializer.save(watchlist=watchlist)
