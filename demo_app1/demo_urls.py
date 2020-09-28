from django.conf.urls import url
from demo_app1.views import UserList, UserDetail, SensorList, SensorDetail, api_root

urlpatterns = [
    url(r'^$', api_root),
    url(r'^user/', UserList.as_view(), name='user-list'),
    url(r'^user1/(?P<pk>[0-9]+)/$', UserDetail.as_view(), name='user-detail'),
    url(r'^sensor/', SensorList.as_view(), name='sensor-list'),
    url(r'^sensor1/(?P<pk>[0-9]+)/$', SensorDetail.as_view(), name='sensor-detail')
]
