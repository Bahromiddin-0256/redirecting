from django.views.generic import TemplateView, RedirectView


class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        print(request)
        return RedirectView.as_view(url=f'http://munir-admin.xn--h28h.uz/?user')(request, *args, **kwargs)

