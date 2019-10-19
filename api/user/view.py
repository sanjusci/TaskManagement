__author__ = "Sanjeev Kumar"
__email__ = "sanju.sci9@gmail.com"
__copyright__ = "Copyright 2019."

import json

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import transaction
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.auth.authentication import TokenAuthentication
from api.function import Function
from api.user.serializers import UserSerializer


class Home(APIView):

    def get(self, request):
        return Response(Function().success_response(
            [],
            'Welcome to Task Management: Task management backend service is '
            'working!!!'
        ),
            status=status.HTTP_200_OK
        )


class Login(APIView):
    """
    Check  credential
    """

    @transaction.atomic
    def post(self, request):
        """
        for login api
        :return:
        """
        try:
            username = request.data["username"]
            password = request.data["password"]
            if User.objects.filter(username=username).exists():
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        token = Token.objects.get_or_create(user=user)
                        user = User.objects.get(username=username)
                        serializer = UserSerializer(instance=user)
                        return Response({
                            "data": serializer.data,
                            "token": str(token[0]),
                            "message": "Token created",
                            "status": status.HTTP_200_OK
                        },
                            status=status.HTTP_200_OK
                        )
                    else:
                        return Response(Function().error_response(
                            [], 'Username is blocked!!'),
                            status=status.HTTP_400_BAD_REQUEST
                        )

                else:
                    return Response(Function().error_response(
                        [], 'Username/ Password not correct!!'),
                        status=status.HTTP_400_BAD_REQUEST
                    )
            else:
                return Response(Function().error_response(
                    [], 'Username does not exist!!'),
                    status=status.HTTP_400_BAD_REQUEST
                )

        except Exception as e:
            return Response(Function().error_response(
                str(e), 'Something went wrong!! Please try again!!'),
                status=status.HTTP_400_BAD_REQUEST
            )


class Logout(APIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self):
        pass


class Users(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, *args, **kwargs):
        try:
            query = {'is_active': True}
            users = User.objects.filter(**query)
            serializer = UserSerializer(instance=users, many=True)
            return Response(Function().success_response(
                serializer.data, 'Users has been fetched successfully!!'),
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(Function().error_response(
                str(e), 'Something went wrong!! Please try again!!'),
                status=status.HTTP_400_BAD_REQUEST
            )