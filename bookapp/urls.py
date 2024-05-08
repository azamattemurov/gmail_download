from django.urls import path
from bookapp.views import books_list_view
from bookapp.views import book_detail_view
from bookapp.views import download_detail_view

app_name = 'books'

urlpatterns = [
    path('', books_list_view, name='list'),
    path('<int:pk>/', book_detail_view, name='detail'),
    path('download/<int:pk>/', download_detail_view, name='download'),

]
