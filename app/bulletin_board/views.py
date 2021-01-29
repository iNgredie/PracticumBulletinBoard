from django.views.generic import TemplateView, CreateView, ListView, UpdateView

from bulletin_board.forms import AdCreateForm


class IndexView(TemplateView):
    template_name = 'index.html'


class AdCreateView(CreateView):
    form_class = AdCreateForm
    template_name = 'create_ad.html'


class AdUpdateView(UpdateView):
    form_class = AdCreateForm
    template_name = 'update_ad.html'


class AdListView(ListView):
    template_name = 'ads_list.html'

