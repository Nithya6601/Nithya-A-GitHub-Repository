from django.contrib import admin
from .models import (Logs, ApacheAccessLogs, ApacheErrorLogs, ApacheAttackLogs, MysqlLogs, MysqlStartupLogs,
                     MysqlShutdownLogs, NginxLogs, NginxAccessLogs, NginxErrorLogs)

# Register your models here.

admin.site.register(Logs)
admin.site.register(ApacheAccessLogs)
admin.site.register(ApacheErrorLogs)
admin.site.register(ApacheAttackLogs)
admin.site.register(MysqlLogs)
admin.site.register(MysqlStartupLogs)
admin.site.register(MysqlShutdownLogs)
admin.site.register(NginxLogs)
admin.site.register(NginxAccessLogs)
admin.site.register(NginxErrorLogs)
