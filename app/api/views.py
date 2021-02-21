from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from api.serializers import AdSerializer
from bulletin_board.models import Ad


class AdListAPIView(generics.ListAPIView):
    """
    Вывод списка объявлений со статусом active
    """
    queryset = Ad.objects.filter(status='active')
    serializer_class = AdSerializer


class AdRetrieveAPIView(generics.RetrieveAPIView):
    """
    Просмотр одного объявления
    """
    queryset = Ad.objects.filter(status='active')
    serializer_class = AdSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        """
        Увеличение количества просмотров.
        Запрещено самому пользователю увеличивать просмотры.
        """
        if self.request.user:
            obj = self.get_object()
            if obj.user != self.request.user:
                obj.views = obj.views + 1
                obj.save(update_fields=('views',))
        return super().get(request, *args, **kwargs)


class AdCreateAPIView(generics.CreateAPIView):
    """
    Создание объявлений
    """
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.validated_data['owner'] = self.request.user
        serializer.save()


class AdUpdateAPIView(generics.UpdateAPIView):
    """
    Обновление обьявления
    """
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        return Ad.objects.filter(owner=self.request.user)


class AdDestroyAPIView(generics.DestroyAPIView):
    """
    Удаление объявления
    """
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        return Ad.objects.filter(onwer=self.request.user)