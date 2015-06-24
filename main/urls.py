from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import views

urlpatterns = [
    # Examples:
    #url(r'^login/$', 'accounts.views.login_view', name='login_view'),
    url(r'^feedback/$', views.feedback, name='feedback'),
    url(r'^company/(?P<key>[0-9]+)/$', views.review, name='review'),
    url(r'^news/(?P<key>[0-9]+)/$', views.new, name='new'),
    url(r'^news/$', views.news, name='news'),
    url(r'^search/$', views.search, name='search'),
    url(r'^$', views.index, name='index'),
    #(r'^success_reset/$','accounts.views.success_reset', name='success_reset'),
   
    #url(r'^invalid_data/$','accounts.views.invalid_data', name='invalid_data'),
    #url(r'^login2/$', 'accounts.views.login_2', name='login_2'),
    #url(r'^logout/$', 'accounts.views.logout_view', name='logout_view'),
    #url(r'^register/$', 'accounts.views.register_view', name='register_view'),
    #url(r'^profile/$', 'accounts.views.settings_view', name='settings_view'),
    #url(r'^password_set/(?P<activation_key>\w+)/$', 'accounts.views.password_view', name='password_view'),
    #url(r'^forgot_password/$', 'accounts.views.forgot_password', name='forgot_password'),
]