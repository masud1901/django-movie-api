from watchlist_app.models import Movie
from rest_framework.response import Response
from django.shortcuts import render
from django.http import JsonResponse
from watchlist_app.api.serializers import MovieSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView


# Class based views
class MovieListAV(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MovieDetailAV(APIView):
    def get(self,request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response(
                {"Error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request,pk):
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie, data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,pk):
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# # Function based view
# @api_view(["GET", "POST"])
# def movie_list(request):
#     if request.method == "GET":
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     if request.method == "POST":
#         serializer = MovieSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(["GET", "PUT", "DELETE"])
# def movie_details(request, pk):
#     if request.method == "GET":
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response(
#                 {"Error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND
#             )
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#     if request.method == "PUT":
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie, data=request.data)
#         if not serializer.is_valid():
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)

#     if request.method == "DELETE":
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
