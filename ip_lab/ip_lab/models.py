from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.


class Institutie(models.Model):

    nume = models.CharField(max_length=100, null=False, blank=False)
    adresa = models.CharField(max_length=500, null=False, blank=False)

    def __str__(self):

        return self.nume


class AgentGuvern(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):

        return self.user.username


class Material(models.Model):

    nume = models.CharField(max_length=100, null=False, blank=False)
    unitati = models.IntegerField(default=0)
    surplus = models.BooleanField(default=False, null=True)
    institutie = models.ForeignKey(
        Institutie, related_name='materiale', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):

        return self.nume




class PromisiuneMaterial(models.Model):

    nume = models.CharField(max_length=100, null=False, blank=False)
    unitati = models.IntegerField(default=0)
    data = models.DateField(null=False, blank=False)
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
