from django.contrib.auth import get_user_model
from rest_framework import generics, viewsets

from api.permissions import OnlyOwnerCanWrite
from ..models import ShelvesModel
from ..serializers import ShelvesSerializer

User = get_user_model()


class ShelvesListView(generics.ListAPIView):
    serializer_class = ShelvesSerializer
    queryset = ShelvesModel.objects.all()

    def get_queryset(self):
        user = generics.get_object_or_404(User, username=self.kwargs.get('username'))
        return self.queryset.filter(user=user)


class ShelfViewSet(viewsets.ModelViewSet):
    serializer_class = ShelvesSerializer
    queryset = ShelvesModel.objects.all()
    permission_classes = [OnlyOwnerCanWrite, ]
    lookup_field = 'slug'

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )
