from django.http import HttpResponsePermanentRedirect
from django.views.generic import TemplateView, RedirectView
import requests


class CustomSchemeRedirect(HttpResponsePermanentRedirect):
    allowed_schemes = ['munirapp', 'https', 'http', 'ftp', 'ftps']


class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        res = requests.get('http://munir-admin.xn--h28h.uz/api/v1/audio_links/retrieve/?link=http://listen.bookmedianashr.uz/shif/index.html?p=1')
        if res.status_code == 200:
            slug = res.json()['product_slug']
            print(slug, f'https://org.uicgroup.munir/product/{slug}')
            return CustomSchemeRedirect(f'https://org.uicgroup.munir/product/{slug}')
        return super().get(request, *args, **kwargs)

