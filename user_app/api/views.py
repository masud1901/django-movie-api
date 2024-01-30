from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from user_app.api.serialisers import RegistrationSerializer
from rest_framework.authtoken.models import Token

# from user_app import models
from rest_framework.decorators import authentication_classes
from rest_framework import mixins, generics, permissions
from rest_framework_simplejwt.tokens import RefreshToken

# @api_view(["POST"])
# def registration_view(request):
#     if request.method == "POST":
#         serializer = RegistrationSerializer(data=request.data)
#         data = {}
#         if serializer.is_valid():
#             account = serializer.save()
#             data = {
#                 "username": account.username,
#                 "email": account.email,
#                 "token": Token.objects.get(user=account).key,
#                 "response": "Registration Successful!",
#             }
#         else:
#             data = serializer.errors
#             return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

#         return Response(data, status=status.HTTP_200_OK)


class RegistrationView(mixins.CreateModelMixin, generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        headers = self.get_success_headers(serializer.data)
        account = serializer.save()
        data = {}
        refresh = RefreshToken.for_user(account)

        data = {
            "username": account.username,
            "email": account.email,
            "refresh_token": str(refresh),
            "access_token": str(refresh.access_token),
            "response": "Registration Successful!",
        }

        return Response(data=data, status=status.HTTP_201_CREATED, headers=headers)


@api_view(["POST"])
def logout_view(request):
    if request.method != "POST":
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.user.is_authenticated:
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
