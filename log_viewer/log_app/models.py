from django.db import models

# Create your models here.


class Logs(models.Model):
    message = models.TextField()
    service = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.service} - {self.created_at}"


class ApacheAccessLogs(models.Model):
    message = models.TextField()
    service = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.service} - {self.created_at}"


class ApacheErrorLogs(models.Model):
    message = models.TextField()
    service = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.service} - {self.created_at}"


class ApacheAttackLogs(models.Model):
    message = models.TextField()
    service = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.service} - {self.created_at}"


class MysqlLogs(models.Model):
    message = models.TextField()
    service = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.service} - {self.created_at}"


class MysqlStartupLogs(models.Model):
    message = models.TextField()
    service = models.CharField(max_length=100)
    msu_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.service} - {self.created_at}"


class MysqlShutdownLogs(models.Model):
    message = models.TextField()
    service = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.service} - {self.created_at}"


class NginxLogs(models.Model):
    message = models.TextField()
    service = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.service} - {self.created_at}"


class NginxAccessLogs(models.Model):
    message = models.TextField()
    service = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.service} - {self.created_at}"


class NginxErrorLogs(models.Model):
    message = models.TextField()
    service = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.service} - {self.created_at}"
