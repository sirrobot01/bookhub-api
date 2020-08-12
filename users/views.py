from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from . import models, serializers


class UserListView(generics.ListAPIView):
    permission_classes = [IsAdminUser, ]
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetailsView(generics.RetrieveUpdateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer

    def get_object(self):
        return generics.get_object_or_404(models.CustomUser, **self.kwargs)
