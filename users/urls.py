from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.UserListView.as_view(), name='users'),
    path('<username>/', views.UserDetailsView.as_view(), name='user')
]
