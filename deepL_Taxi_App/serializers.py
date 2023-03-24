from rest_framework import serializers
from .models import Agent
#from .models import Qitem

    
class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Agent
        fields='__all__' #serializes all fields
        
        
