from django.urls import path

from bulletin_board.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index')
]