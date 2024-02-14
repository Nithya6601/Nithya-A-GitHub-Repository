from django.urls import path
from . import views

urlpatterns = [
    path('', views.log, name='log'),
    path('apache', views.apache_logs, name='apache_logs'),
    path('apache_access_logs', views.apache_access_logs, name='apache_access_logs'),
    path('apache_error_logs', views.apache_error_logs, name='apache_error_logs'),
    path('apache_attack_logs', views.apache_attack_logs, name='apache_attack_logs'),
    path('mysql_logs', views.mysql_logs, name='mysql_logs'),
    path('mysql_startup_logs', views.mysql_startup_logs, name='mysql_startup_logs'),
    path('mysql_shutdown_logs', views.mysql_shutdown_logs, name='mysql_shutdown_logs'),
    path('nginx_logs', views.nginx_logs, name='nginx_logs'),
    path('nginx_access_logs', views.nginx_access_logs, name='nginx_access_logs'),
    path('nginx_error_logs', views.nginx_error_logs, name='nginx_error_logs'),

]
