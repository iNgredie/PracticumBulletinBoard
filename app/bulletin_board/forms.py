from django.forms import ModelForm

from bulletin_board.models import Ad


class AdCreateUpdateForm(ModelForm):
    class Meta:
        model = Ad
        fields = ("title", "category", "city", "description", "price", "status")
