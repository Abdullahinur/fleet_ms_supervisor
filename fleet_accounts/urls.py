from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url('^$', views.home, name='home'),
    url(r'^saccos/(?P<pk>\d+)/$', views.sacco, name='sacco'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
