from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from django_filters import rest_framework as filters
from ip_lab.ip_lab.serializers import *


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class MaterialViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('surplus', 'institutie')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PromisiuneMaterialViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = PromisiuneMaterial.objects.all()
    serializer_class = PromisiuneMaterialSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SoferViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Sofer.objects.all()
    serializer_class = SoferSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AdministratorViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Administrator.objects.all()
    serializer_class = AdministratorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AgentGuvernViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = AgentGuvern.objects.all()
    serializer_class = AgentGuvernSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class InstitutieViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Institutie.objects.all()
    serializer_class = InstitutieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
