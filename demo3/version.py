from django.conf.urls import url, include
from demo_app1 import demo_urls

urlpatterns = [
    url(r'v1/', include(demo_urls)),
]
