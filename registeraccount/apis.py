# registeraccount/apis.py

from rest_framework import generics
from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework import status

class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()  # Save the user

        return Response({
            'username': user.username,
            'email': user.email,
            'message': 'Registration successful!',
        }, status=status.HTTP_201_CREATED)
