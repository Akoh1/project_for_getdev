from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.book_list, name='book_list'),
    path('books/create', views.book_create, name='book_new'),
    path('<int:rate_id>/rate/', views.rate, name='rate'),
    path('books/<int:book_id>/update/', views.book_update, name='book_update'),
    path('books/<int:book_id>/delete/', views.book_delete, name='book_delete'),
]
