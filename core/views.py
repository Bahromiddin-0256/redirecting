import json

from django.http import HttpResponsePermanentRedirect
from django.views.generic import TemplateView, RedirectView
import requests
from django.utils.html import mark_safe

class CustomSchemeRedirect(HttpResponsePermanentRedirect):
    allowed_schemes = ['munirapp', 'https', 'http', 'ftp', 'ftps']


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url = 'http://listen.bookmedianashr.uz/shif/index.html?p=1'
        api = f'http://munir-admin.xn--h28h.uz/api/v1/audio_links/retrieve/'
        context['api'] = api
        context['url'] = url
        context['red_url'] = 'munirapp://org.uicgroup.munir/product/ghdsfj'
        res = requests.get(f'http://munir-admin.xn--h28h.uz/api/v1/audio_links/retrieve/?link={url}')
        if res.status_code == 200:
            context['data'] = mark_safe(json.dumps(res.json()))
        return context

    def get(self, request, *args, **kwargs):

        return super().get(request, *args, **kwargs)


