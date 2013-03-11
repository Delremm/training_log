from django.db import models

class Model_field_got_value_ach(models.Model):
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    field = models.CharField(max_length=255)
    field_type = models.CharField(max_length=255)
    value = models.CharField(max_length=255)


