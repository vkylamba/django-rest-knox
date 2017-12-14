from django.conf.urls import include, url
from django.contrib import admin

from .views import RootView

urlpatterns = [
    url(r'^api/', include('knox.urls')),
    url(r'^api/$', RootView.as_view(), name="api-root"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(admin.site.urls)),
]
