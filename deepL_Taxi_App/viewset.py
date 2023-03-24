from deepL_Taxi_App.serializers import AgentSerializer
from rest_framework import viewsets
from .models import Agent


class AgentViewSet(viewsets.ModelViewSet):

    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    http_method_name = ['get', 'post', 'put', 'delete','patch']