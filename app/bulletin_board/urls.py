from django.contrib.auth.decorators import login_required
from django.urls import path

from bulletin_board.views import (AdCreateView, AdDetailView, AdListView,
                                  AdUpdateView, IndexView)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("create/", login_required(AdCreateView.as_view()), name="create"),
    path("update/<int:pk>/", login_required(AdUpdateView.as_view()), name="update"),
    path("list/", AdListView.as_view(), name="list"),
    path("list/<int:pk>/", AdDetailView.as_view(), name="detail"),
]
