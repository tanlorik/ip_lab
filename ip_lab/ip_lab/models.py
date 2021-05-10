from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.


class Institutie(models.Model):

    nume = models.CharField(max_length=100, null=False, blank=False)
    adresa = models.CharField(max_length=500, null=False, blank=False)
    logitudine = models.FloatField(default=0)
    latitudine = models.FloatField(default=0)

    def __str__(self):

        return self.nume


class AgentGuvern(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):

        return self.user.username


class TipMaterial(models.Model):

    nume = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):

        return self.nume


class Material(models.Model):

    tip = models.ForeignKey(
        TipMaterial, related_name='tip_material', blank=True, null=True, on_delete=models.CASCADE)
    unitati = models.IntegerField(default=0)
    surplus = models.BooleanField(default=False, null=True)
    institutie = models.ForeignKey(
        Institutie, related_name='materiale', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):

        return self.nume


class PromisiuneMaterial(models.Model):

    tip_material = models.ForeignKey(
        TipMaterial, blank=True, null=True, on_delete=models.CASCADE)
    unitati = models.IntegerField(default=0)
    data = models.DateTimeField(null=False, blank=False)
    institutie = models.ForeignKey(
        Institutie, related_name='promisiune', on_delete=models.CASCADE)
    agent = models.ForeignKey(
        AgentGuvern, related_name='agent', on_delete=models.CASCADE)

    def __str__(self):

        return self.nume


class Sofer(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ora_start = models.IntegerField(default=0)
    ora_sfarsit = models.IntegerField(default=0)
    disponibil = models.BooleanField(default=False, null=True)
    institutie = models.ForeignKey(
        Institutie, related_name='soferi', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):

        return self.user.username


class Administrator(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    institutie = models.ForeignKey(
        Institutie, related_name='administratori', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):

        return self.user.username


class Istoric(models.Model):

    institutie_donatoare = models.ForeignKey(
        Institutie, related_name='donator', blank=True, null=True, on_delete=models.CASCADE)
    institutie_primitoare = models.ForeignKey(
        Institutie, related_name='primitor', blank=True, null=True, on_delete=models.CASCADE)
    data_cerere = models.DateTimeField(null=False, blank=False)
    data_plecare_sofer = models.DateTimeField(null=False, blank=False)
    data_livrare = models.DateTimeField(null=False, blank=False)
    tip_material = models.ForeignKey(
        TipMaterial, blank=True, null=True, on_delete=models.CASCADE)
    cantitate = models.IntegerField(default=0)
    sofer = models.ForeignKey(
        Sofer, blank=True, null=True, on_delete=models.CASCADE)


class Cerere(models.Model):

    institutie = models.ForeignKey(
        Institutie, blank=True, null=True, on_delete=models.CASCADE)
    data_cerere = models.DateTimeField(null=False, blank=False)
    data_limita = models.DateTimeField(null=False, blank=False)
    tip_material = models.ForeignKey(
        TipMaterial, blank=True, null=True, on_delete=models.CASCADE)
    cantitate = models.IntegerField(default=0)
    prioritate = models.IntegerField(default=0)
