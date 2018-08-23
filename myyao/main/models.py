from django.db import models

class Countdown(models.Model):
    years = models.IntegerField(verbose_name='年',default=0, db_index = True, unique=True)
    months = models.IntegerField(verbose_name='月',default=0, db_index = True, unique=True)
    days = models.IntegerField(verbose_name='日',default=0, db_index = True, unique=True)
    hours = models.IntegerField(verbose_name='时',default=0, db_index = True, unique=True)
    minutes = models.IntegerField(verbose_name='分',default=0, db_index = True, unique=True)
    seconds = models.IntegerField(verbose_name='秒',default=0, db_index = True, unique=True)