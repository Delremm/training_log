from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Entry(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.title

from mptt.managers import TreeManager
class CustomTreeManager(TreeManager):
    def get_query_set(self):
        order = self.tree_id_attr
        return super(CustomTreeManager, self).get_query_set().order_by(
            order, self.left_attr)

class Massage(MPTTModel):

    title = models.CharField(max_length=255)
    parent = TreeForeignKey('self', blank=True, null=True)

    #class MPTTMeta:
        #order_insertion_by = 'pk'


    def get_absolute_url(self):
        return "/board/%s/" % self.id

from django.contrib import admin
admin.site.register(Entry)
admin.site.register(Massage)