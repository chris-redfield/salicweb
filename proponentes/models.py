# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Proponente(models.Model):
    idusuario = models.IntegerField(primary_key=True)
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=100)
    dtnascimento = models.DateField()
    email = models.CharField(max_length=60)
    senha = models.CharField(max_length=15)
    dtcadastro = models.DateField()
    situacao = models.IntegerField()
    dtsituacao = models.DateField()

    def __str__(self):
        return self.nome

    class Meta:
        managed = False
        db_table = 'sgcacesso'
