from django.db import models


class KVStore(models.Model):
    key = models.CharField(max_length=200, primary_key=True)
    value = models.TextField()
    class Meta:
        db_table = 'thumbnail_kv_store_test'
