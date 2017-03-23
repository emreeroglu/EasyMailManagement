from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from web import views

urlpatterns = i18n_patterns(
    url(r'^admin/', admin.site.urls),
    url(r'^servers/', views.servers, name='servers'),
    url(r'^add_server/', views.add_server, name='add_server'),
    url(r'^login/$', views.login_page, name='login'),
    url(r'^logout/$', views.logout_page, name='logout'),
    url(r'^register/$', views.register_page, name='register'),
    url(r'^$', views.index, name='index'),
)

urlpatterns += {
    url(r'^ajax/check_username/$',  views.check_username, name='check_username'),
}