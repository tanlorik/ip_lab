from django.contrib.auth.models import User, Group
from rest_framework import serializers
from ip_lab.ip_lab.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'groups']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'url', 'name']


class MaterialSerializer(serializers.ModelSerializer):

    # institutie = serializers.StringRelatedField(many=False)

    class Meta:
        model = Material
        fields = ['id', 'nume', 'unitati', 'surplus', 'institutie']


class PromisiuneMaterialSerializer(serializers.ModelSerializer):

    # institutie = serializers.StringRelatedField(many=False)
    # agent = serializers.StringRelatedField(many=False)

    class Meta:
        model = PromisiuneMaterial
        fields = ['id', 'nume', 'unitati', 'data', 'institutie', 'agent']


class SoferSerializer(serializers.ModelSerializer):

    # institutie = serializers.StringRelatedField(many=False)
    # user = serializers.StringRelatedField(many=False)

    class Meta:
        model = Sofer
        fields = ['id', 'user', 'ora_start', 'ora_sfarsit', 'institutie']


class AdministratorSerializer(serializers.ModelSerializer):

    # institutie = serializers.StringRelatedField(many=False)
    # user = serializers.StringRelatedField(many=False)

    class Meta:
        model = Administrator
        fields = ['id', 'user', 'institutie']


class AgentGuvernSerializer(serializers.ModelSerializer):

    # user = serializers.StringRelatedField(many=False)

    class Meta:
        model = AgentGuvern
        fields = ['id', 'user']


class InstitutieSerializer(serializers.ModelSerializer):

    administratori = serializers.IntegerField(many=True)
    soferi = serializers.IntegerField(many=True)

    class Meta:
        model = Institutie
        fields = ['id', 'nume', 'adresa', 'administratori', 'soferi']
