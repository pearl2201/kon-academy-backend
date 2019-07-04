from django.conf.urls import url
from django.urls import include, path
from .views import AssetPackageView,AssetPackageDetailView
urlpatterns = [
    url(r'^assets/$', AssetPackageView.as_view(), name='asset-view'),
    url(r'^assets/(?P<pk>\d+)/$', AssetPackageDetailView.as_view(), name='asset-detail-view'),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls'))
]
