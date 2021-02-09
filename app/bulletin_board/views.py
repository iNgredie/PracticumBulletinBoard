from django.views.generic import (CreateView, DetailView, ListView,
                                  TemplateView, UpdateView)

from bulletin_board.forms import AdCreateUpdateForm
from bulletin_board.models import Ad


class IndexView(TemplateView):
    template_name = "index.html"


class AdCreateView(CreateView):
    form_class = AdCreateUpdateForm
    template_name = "create_ad.html"
    success_url = "/list/"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        self.object = form.save()
        return super(AdCreateView, self).form_valid(form)


class AdUpdateView(UpdateView):
    model = Ad
    form_class = AdCreateUpdateForm
    template_name = "update_ad.html"
    success_url = "/list/"

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.model.objects.filter(owner=self.request.user)


class AdListView(ListView):
    model = Ad
    template_name = "list_ads.html"


class AdDetailView(DetailView):
    model = Ad
    template_name = "detail_ad.html"
