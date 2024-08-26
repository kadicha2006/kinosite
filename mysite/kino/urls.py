from django.urls import path
from .views import *




urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),


    path('userProfile/', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='user_list'),
    path('userProfile/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='user_detail'),
    path('countries/', CountryViewSet.as_view({'get': 'list', 'post': 'create'}), name='country_list'),
    path('countries/<int:pk>/', CountryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='country_detail'),
    path('directors/', DirectorViewSet.as_view({'get': 'list', 'post': 'create'}), name='director_list'),
    path('directors/<int:pk>/', DirectorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='director_detail'),
    path('actors/', ActorViewSet.as_view({'get': 'list', 'post': 'create'}), name='actor_list'),
    path('actors/<int:pk>/', ActorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='actor_detail'),
    path('genres/', GenreViewSet.as_view({'get': 'list', 'post': 'create'}), name='genre_list'),
    path('genres/<int:pk>/', GenreViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='genre_detail'),

    path('', MovieViewSet.as_view({'get': 'list', 'post': 'create'}), name='movie_list'),
    path('movies/<int:pk>/', MovieViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='movie_detail'),

    path('ratings/', RatingViewSet.as_view({'get': 'list', 'post': 'create'}), name='rating_list'),
    path('ratings/<int:pk>/', RatingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='rating_detail'),
    path('comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='comment_list'),
    path('comments/<int:pk>/', CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='comment_detail'),
    path('cart/', CartViewSet.as_view({'get': 'retrieve'}), name='cart_detail'),
    path('cart_items/', CartItemViewSet.as_view({'get': 'list', 'post': 'create'}), name='cart_item_list'),
    path('cart_items/<int:pk>/', CartItemViewSet.as_view({'put': 'update', 'delete': 'destroy'}),
         name='cart_item_detail'),
]
