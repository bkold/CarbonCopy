from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ribbit_app.views.index', name='b'),
    url(r'^login$', 'ribbit_app.views.login_view', name='logn'),
    url(r'^logout$', 'ribbit_app.views.logout_view', name='logot'),
    url(r'^signup$', 'ribbit_app.views.signup', name='sign'),
    url(r'^public$', 'ribbit_app.views.public', name='pub'),
    url(r'^submit$', 'ribbit_app.views.submit', name='sub'),
    url(r'^users/$', 'ribbit_app.views.users', name='us'),
    url(r'^users/(?P<username>\w{0,30})/$', 'ribbit_app.views.users', name='ussp'),
    url(r'^follow$', 'ribbit_app.views.follow', name='fol'),
    # url(r'^ribbit/', include('ribbit.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
