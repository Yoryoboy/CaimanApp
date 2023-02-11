from django.db import models

# Create your models here.
class Accounts(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='name')
    mail = models.EmailField(max_length=100, verbose_name='enail')
    password = models.CharField(max_length=100, verbose_name='password')
    phone = models.CharField(max_length=100, verbose_name='phone')
