from django.contrib.auth.models import User, Group
from rest_framework import serializers
from ip_lab.ip_lab.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'groups', 'password']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'url', 'name']


class TipMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipMaterial
        fields = ['id', 'nume']


class MaterialSerializer(serializers.ModelSerializer):

    # institutie = serializers.StringRelatedField(many=False)

    class Meta:
        model = Material
        fields = ['id', 'tip', 'unitati', 'surplus', 'institutie']


class PromisiuneMaterialSerializer(serializers.ModelSerializer):

    # institutie = serializers.StringRelatedField(many=False)
    # agent = serializers.StringRelatedField(many=False)

    class Meta:
        model = PromisiuneMaterial
        fields = ['id', 'tip_material', 'unitati',
                  'data', 'institutie', 'agent']


class SoferSerializer(serializers.ModelSerializer):

    # institutie = serializers.StringRelatedField(many=False)
    # user = serializers.StringRelatedField(many=False)

    class Meta:
        model = Sofer
        fields = ['id', 'user', 'ora_start',
                  'ora_sfarsit', 'institutie', 'disponibil']


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

    administratori = serializers.StringRelatedField(many=True)
    soferi = serializers.StringRelatedField(many=True)

    class Meta:
        model = Institutie
        fields = ['id', 'nume', 'adresa', 'administratori',
                  'soferi', 'logitudine', 'latitudine']


class IstoricSerializer(serializers.ModelSerializer):

    class Meta:
        model = Istoric
        fields = ['id', 'institutie_donatoare', 'institutie_primitoare',
                  'data_cerere', 'data_plecare_sofer', 'data_livrare', 'tip_material', 'cantitate', 'sofer']


class CerereSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cerere
        fields = ['id', 'institutie', 'data_cerere',
                  'data_limita', 'tip_material', 'cantitate', 'prioritate']
