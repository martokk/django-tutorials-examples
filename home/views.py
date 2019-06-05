from django.shortcuts import render

from django.conf import settings
from django.urls import URLPattern, URLResolver

urlconf = __import__(settings.ROOT_URLCONF, {}, {}, [''])

def list_urls(lis, acc=None):
    if acc is None:
        acc = []
    if not lis:
        return
    l = lis[0]
    if isinstance(l, URLPattern):
        yield acc + [str(l.pattern)]
    elif isinstance(l, URLResolver):
        yield from list_urls(l.url_patterns, acc + [str(l.pattern)])

    yield from list_urls(lis[1:], acc)




def home(request):
    from django.conf import settings
    from tutorials.urls import urlpatterns

    from django.urls import get_resolver


    urlpatterns = set(v[1] for k,v in get_resolver(None).reverse_dict.items())

    default_apps = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]

    user_apps = [app for app in settings.INSTALLED_APPS if app not in default_apps]



    vars = {
        'urlpatterns': urlpatterns,
        'default_apps': default_apps,
        'user_apps': user_apps,
    }

    return render(request, 'home/home.html', vars)
