from django.conf.urls import patterns, url
from ppayment import views

urlpatterns = patterns('',
                url(r'^$', views.index, name='index'),
                url(r'^success/', views.success, name='success'),
                url(r'^cancel/', views.cancel, name='cancel'),
                url(r'^notify/', views.notify, name='notify'),
                url(r'^login/$', views.user_login, name='login'),
                #url(r'^loginme/$',views.login_view, name='loginme'),
                url(r'^orders/', views.login_view, name='orders'),
                url(r'^logout/$', views.logout_view, name='logout'),
)
