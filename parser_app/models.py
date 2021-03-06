from django.db import models
from django.utils import timezone


class PricesRaw(models.Model):

    date = models.DateTimeField('date', default=timezone.now)
    type = models.TextField('type', default='')
    category_id = models.IntegerField('category_id', default=0)
    category_title = models.TextField('category_title', default='')
    site_title = models.TextField('site_title', default='')
    price_new = models.FloatField('price_new', default=-1.0)
    price_old = models.FloatField('price_old', default=-1.0)
    site_unit = models.TextField('site_unit', default='')
    site_link = models.TextField('site_link', default='')
    site_code = models.TextField('site_code', default='')
    miss = models.IntegerField('miss', default=0)

    class Meta:
        ordering = ('date',)


class PricesProcessed(models.Model):

    date = models.DateTimeField('date', default=timezone.now)
    type = models.TextField('type', default='')
    category_id = models.IntegerField('category_id', default=0)
    category_title = models.TextField('category_title', default='')
    site_title = models.TextField('site_title', default='')
    price_new = models.FloatField('price_new', default=-1.0)
    nsprice_f = models.FloatField('nsprice_f', default=-1.0)
    price_old = models.FloatField('price_old', default=-1.0)
    site_unit = models.TextField('site_unit', default='')
    site_link = models.TextField('site_link', default='')
    site_code = models.TextField('site_code', default='')
    miss = models.IntegerField('miss', default=0)

    class Meta:
        ordering = ('date',)


class Gks(models.Model):

    date = models.DateTimeField('date', default=timezone.now)
    type = models.TextField('type', default='')
    category_id = models.IntegerField('category_id', default=0)
    category_title = models.TextField('category_title', default='')
    site_title = models.TextField('site_title', default='')
    price_new = models.FloatField('price_new', default=-1.0)
    price_old = models.FloatField('price_old', default=-1.0)
    site_unit = models.TextField('site_unit', default='')
    site_link = models.TextField('site_link', default='')
    site_code = models.TextField('site_code', default='')
    miss = models.IntegerField('miss', default=0)

    class Meta:
        ordering = ('date',)


class Basket(models.Model):

    date = models.DateTimeField('date', default=timezone.now)
    gks_price = models.FloatField('price_new', default=-1.0)
    online_price = models.FloatField('price_new', default=-1.0)

    class Meta:
        ordering = ('date',)
