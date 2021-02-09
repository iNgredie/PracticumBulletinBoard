from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DetailView

from bulletin_board.forms import AdCreateForm
from bulletin_board.models import Ad


class IndexView(TemplateView):
    template_name = 'index.html'


class AdCreateView(CreateView):
    form_class = AdCreateForm
    template_name = 'create_ad.html'
    success_url = '/'


class AdDetailView(DetailView):
    model = Ad
    template_name = 'detail_ad.html'
    success_url = '/'


class AdUpdateView(UpdateView):
    model = Ad
    form_class = AdCreateForm
    template_name = 'update_ad.html'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.model.objects.filter(owner=self.request.user)


class AdListView(ListView):
    model = Ad
    template_name = 'list_ads.html'

