from django.forms import ModelForm

from bulletin_board.models import Ad


class AdCreateForm(ModelForm):
    class Meta:
        model = Ad
        fields = ('title', 'category', 'city', 'description', 'price', 'owner', 'status')
