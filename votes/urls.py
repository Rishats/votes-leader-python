from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^votes_leader/', include('votes_leader.urls')),
    url(r'^admin/', admin.site.urls),
]
