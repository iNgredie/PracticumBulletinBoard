from django.urls import path

from bulletin_board.views import IndexView, AdCreateView, AdUpdateView, AdListView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create/', AdCreateView.as_view(), name='create'),
    path('update/', AdUpdateView.as_view(), name='update'),
    path('list/', AdListView.as_view(), name='list'),
]


