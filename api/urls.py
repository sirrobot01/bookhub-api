from django.urls import path, include

from .views import shelves, books
from rest_framework import routers

router = routers.SimpleRouter()
router.register('shelf', shelves.ShelfViewSet)

urlpatterns = [
    path('users/', include('users.urls')),
    path('shelves/<username>/', shelves.ShelvesListView.as_view()),
    path('', include(router.urls)),

    path('<username>/books/', books.UserBooksView.as_view(), name='user-books'),
    path('<username>/book/<slug>/', books.UserGetAndUpdateView.as_view(), name='user-view'),
    path('book/', books.UserCreateView.as_view(), name='create-book'),
    path('books/', books.book_query, name='query-book')
]
