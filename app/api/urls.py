from django.urls import path

from api.views import AdCreateAPIView, AdUpdateAPIView, AdListAPIView, AdRetrieveAPIView, AdDestroyAPIView

urlpatterns = [
    path('ad/', AdListAPIView.as_view(), name='list ad'),
    path('ad/<pk>/', AdRetrieveAPIView.as_view(), name='retrieve ad'),
    path('ad/', AdCreateAPIView.as_view(), name='create ad'),
    path('ad/<pk>', AdUpdateAPIView.as_view(), name='update ad'),
    path('ad/', AdDestroyAPIView.as_view(), name='delete ad'),
]
