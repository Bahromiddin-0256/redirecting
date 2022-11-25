import json

import requests
from django.http import HttpResponsePermanentRedirect
from django.utils.html import mark_safe
from django.views.generic import TemplateView
from main.models import Settings


class CustomSchemeRedirect(HttpResponsePermanentRedirect):
    allowed_schemes = ['munirapp', 'https', 'http', 'ftp', 'ftps']


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        setting, _c = Settings.objects.get_or_create(pk=1)
        if setting.use_example_link:
            url = setting.example_link
        else:
            url = self.request.build_absolute_uri()
        api = f'http://munir-admin.xn--h28h.uz/api/v1/audio_links/retrieve/'
        context['api'] = api
        context['url'] = url
        context['red_url'] = 'munirapp://audiobook/product_slug/'
        res = requests.get(f'http://munir-admin.xn--h28h.uz/api/v1/audio_links/retrieve/?link={url}')
        if res.status_code == 200:
            context['data'] = mark_safe(json.dumps(res.json()))
        return context

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
