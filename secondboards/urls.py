from django.urls import path
from .views import *
from .models import Board

app_name = 'secondboard'

urlpatterns = [
    path('', BoardListView.as_view(), name='board_list'),
    path('detail/<int:pk>', BoardDetailView.as_view(), name='board_detail'),
    path('upload/', BoardUploadView.as_view(), name='board_upload'),
    path('delete/<int:pk>', BoardDeleteView.as_view(), name='board_delete'),
    path('update/<int:pk>', BoardUpdateView.as_view(), name='board_update'),
]
