from django.conf.urls import url, include
from django.contrib import admin
from .views import IndexPage

urlpatterns = [
    url(r'^$', IndexPage.as_view(), name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^bookmark/', include("bookmark.urls", namespace="bookmark")),
]
