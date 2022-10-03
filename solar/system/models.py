from django.db import models


class Resistence(models.Model):
    time = models.DateTimeField(db_column='time')  # Field name made lowercase.
    value = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resistence'


class Indications(models.Model):
    time = models.DateTimeField(db_column='time')  # Field name made lowercase.
    name = models.CharField(db_column='name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    value = models.CharField(db_column='value', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'system_indications'


class Current(models.Model):
    time = models.DateTimeField(db_column='time')  # Field name made lowercase.
    value = models.CharField(db_column='value', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'current'



