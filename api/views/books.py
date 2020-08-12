from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..models import BookModel, ShelvesModel, CategoryModel
from ..permissions import OnlyOwnerCanWrite
from ..serializers import BookSerializer

User = get_user_model()


class UserBooksView(generics.ListAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        user = generics.get_object_or_404(User, username=self.kwargs.get('username'))
        return self.queryset.filter(user=user)


@api_view(['GET'])
@renderer_classes((JSONRenderer, BrowsableAPIRenderer))
def book_query(request):
    if request.method == 'GET':
        queries = request.GET
        shelves = ShelvesModel.objects.filter(slug__in=queries.getlist('shelf'))
        categories = CategoryModel.objects.filter(slug__in=queries.getlist('category'))
        kwargs = {}
        if shelves:
            kwargs.update({'shelf__in': shelves})
        elif categories:
            kwargs.update({'category__in': categories})
        queryset = BookModel.objects.filter(**kwargs)
        print(queryset)
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({"detail": f'Method {request.method} not allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class UserGetAndUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        user = generics.get_object_or_404(User, username=self.kwargs.get('username'))
        slug = self.kwargs.get('slug')
        return self.queryset.filter(user=user, slug=slug)


class UserCreateView(generics.CreateAPIView):
    serializer_class = BookSerializer
    queryset = BookModel.objects.all()
    permission_classes = [OnlyOwnerCanWrite, ]

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )
