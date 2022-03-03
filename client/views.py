from rest_framework import viewsets

from .models import Client
from .serializers import ClientSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)
