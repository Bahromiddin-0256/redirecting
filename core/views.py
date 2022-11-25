from django.http import HttpResponsePermanentRedirect
from django.views.generic import TemplateView, RedirectView
import requests


class CustomSchemeRedirect(HttpResponsePermanentRedirect):
    allowed_schemes = ['munirapp', 'https', 'http', 'ftp', 'ftps']


class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        url = request.build_absolute_uri()
        res = requests.get(f'http://munir-admin.xn--h28h.uz/api/v1/audio_links/retrieve/?link={url}')
        print(url)
        BOT_TOKEN = "5767150172:AAEj5dBCDjgMWG_p0dXuy_GtyTw2-DsHJXE"
        requests.get(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id=1204383599&text={url}"
        )
        if res.status_code == 200:
            slug = res.json()['product_slug']
            return CustomSchemeRedirect(f'munirapp://org.uicgroup.munir/product/ghdsfj')

        return CustomSchemeRedirect(f'munirapp://org.uicgroup.munir/')

