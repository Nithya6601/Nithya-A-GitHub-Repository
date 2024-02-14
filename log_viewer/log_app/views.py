from django.shortcuts import render
from .models import Logs, ApacheAccessLogs, ApacheErrorLogs, ApacheAttackLogs, MysqlLogs, MysqlStartupLogs, MysqlShutdownLogs, NginxLogs, NginxAccessLogs, NginxErrorLogs
from django.core.paginator import Paginator

# Create your views here.


def log(request):

    return render(request,"index.html")


def apache_logs(request):
    logs = Logs.objects.all()
    page = Paginator(logs,10)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    context = {
        'page': page,
    }
    return render(request, "apache.html", context)


def apache_access_logs(request):
    logs = ApacheAccessLogs.objects.all()
    page = Paginator(logs,10)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    context = {
        'page': page,
    }
    return render(request, "apache_access.html", context)


def apache_error_logs(request):
    logs = ApacheErrorLogs.objects.all()
    page = Paginator(logs,10)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    context = {
        'page': page,
    }
    return render(request, "apache_error.html", context)


def apache_attack_logs(request):
    logs = ApacheAttackLogs.objects.all()
    page = Paginator(logs,5)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    context = {
        'page': page,
    }
    return render(request, "apache_attack.html", context)


def mysql_logs(request):
    logs = MysqlLogs.objects.all()
    page = Paginator(logs,10)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    context = {
        'page': page,
    }
    return render(request, "mysql.html", context)


def mysql_startup_logs(request):
    logs = MysqlStartupLogs.objects.all()
    page = Paginator(logs,10)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    context = {
        'page': page,
    }
    return render(request, "mysql_startup.html", context)


def mysql_shutdown_logs(request):
    logs = MysqlShutdownLogs.objects.all()
    page = Paginator(logs,10)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    context = {
        'page': page,
    }
    return render(request, "mysql_shutdown.html", context)


def nginx_logs(request):
    logs = NginxLogs.objects.all()
    page = Paginator(logs,10)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    context = {
        'page': page,
    }
    return render(request, "nginx.html", context)


def nginx_access_logs(request):
    logs = NginxAccessLogs.objects.all()
    page = Paginator(logs,10)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    context = {
        'page': page,
    }
    return render(request, "nginx_access.html", context)


def nginx_error_logs(request):
    logs = NginxErrorLogs.objects.all()
    page = Paginator(logs,10)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    context = {
        'page': page,
    }
    return render(request, "nginx_error.html", context)
