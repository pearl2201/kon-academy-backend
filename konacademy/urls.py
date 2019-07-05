from django.conf.urls import url
from django.urls import include, path
from .views import AssetPackageView,AssetPackageDetailView, BookPackageView, BookPackageDetailView, CategoryPackageView, CategoryPackageDetailView
urlpatterns = [
    url(r'^assets/$', AssetPackageView.as_view(), name='asset-view'),
    url(r'^assets/(?P<pk>\d+)/$', AssetPackageDetailView.as_view(), name='asset-detail'),
    url(r'^category/$', CategoryPackageView.as_view(), name='category-view'),
    url(r'^category/(?P<pk>\d+)/$', CategoryPackageDetailView.as_view(), name='category-detail'),
    url(r'^book/$', BookPackageView.as_view(), name='book-view'),
    url(r'^book/(?P<pk>\d+)/$', BookPackageDetailView.as_view(), name='book-detail'),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls'))
]
