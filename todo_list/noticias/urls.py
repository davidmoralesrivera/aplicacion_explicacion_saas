from django.conf.urls import url

from .views import LandingPageView

app_name = 'noticias'

urlpatterns = [
    url(r'^$', LandingPageView.as_view(), name='landing'),
]
