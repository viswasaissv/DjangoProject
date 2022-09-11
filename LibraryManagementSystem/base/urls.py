from django.urls import path
from .views import CustomLoginView,BookDelete, BookDetail, BookList,BookCreate,BookUpdate,RegisterPage
from django.contrib.auth.views import LogoutView
urlpatterns=[
    path('login/',CustomLoginView.as_view(),name='login'),
    path('register/',RegisterPage.as_view(),name='register'), 
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('',BookList.as_view(),name='books'),
    path('book/<int:pk>/',BookDetail.as_view(),name='book'),
    path('book-create/',BookCreate.as_view(),name='book-create'), 
    path('book-update/<int:pk>/',BookUpdate.as_view(),name='book-update'), 
    path('book-delete/<int:pk>/',BookDelete.as_view(),name="book-delete"),
]