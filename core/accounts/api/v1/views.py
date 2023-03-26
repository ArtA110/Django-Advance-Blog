from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView
from . import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from accounts.models import Profile
from django.shortcuts import get_object_or_404
from mail_templated import EmailMessage
from ..utils import EmailThread
from rest_framework_simplejwt.tokens import RefreshToken
import jwt
from jwt.exceptions import InvalidTokenError, ExpiredSignatureError
from django.conf import settings


User = get_user_model()


class RegistrationApiView(GenericAPIView):
    serializer_class = serializers.RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            email = serializer.validated_data['email']
            data = {
                'email': email
            }
            user = get_object_or_404(User, email=email)
            token = self.get_tokens_for_user(user)
            email_obj = EmailMessage('email/Activation.tpl', {'token': token}, 'ali.tabatabaeian16@gmail.com',
                                     to=[email])
            EmailThread(email_obj).start()
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)

        return str(refresh.access_token)



class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key,
                         'email': user.email,
                         'id': user.pk})


class CustomDiscardAuthToken(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = serializers.CustomTokenOptainPairSerializer


class ChangePasswordApiView(GenericAPIView):
    serializer_class = serializers.ChangePasswordSerializer
    permission_classes = [IsAuthenticated]
    model = User

    def get_object(self, queryset=None):
        return self.request.user

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.validated_data.get('old_password')):
                return Response({'old_password': 'wrong password'}, status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.validated_data.get('new_password'))
            self.object.save()
            return Response({'new_password': 'password set successfully!'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileApiView(RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer


    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj


class ConfirmActivationApiView(APIView):
    def get(self, request, token, *args, **kwargs):
        try:
            decode_token = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user_id = decode_token.get('user_id')
        except ExpiredSignatureError:
            return Response({'details': 'Your activation token has expired!'})
        except InvalidTokenError:
            return Response({'details': 'Your activation token is not valid!'})
        user = get_object_or_404(User, pk=user_id)
        if user.is_verified:
            return Response({'details': 'You have been already verified!'})
        user.is_verified = True
        user.save()
        return Response({'details': 'User have been verified'})


class ResendActivationApiView(GenericAPIView):
    serializer_class = serializers.ResendActivationSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        if user.is_verified:
            return Response({'details': 'Already verified'}, status=status.HTTP_400_BAD_REQUEST)
        token = self.get_tokens_for_user(user)
        email_obj = EmailMessage('email/Activation.tpl', {'token': token}, 'ali.tabatabaeian16@gmail.com',
                                 to=[user.email])
        EmailThread(email_obj).start()
        return Response({'details': 'Email resend successfully'}, status=status.HTTP_200_OK)

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)

        return str(refresh.access_token)