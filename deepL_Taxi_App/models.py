from django.db import models
from django.db.models import IntegerField 
from collections import defaultdict
import numpy as np
from drf_compound_fields.fields import ListField

""""
class Qitem(models.Model):
    action = IntegerField(default=0)
    state = IntegerField(default=1)"""
    
    
    
class Agent(models.Model):
    epsilon=models.FloatField(null=False,blank=False,default=1)
    learning_rate=models.FloatField(null=False,blank=False,default=0.9)
    discount_rate=models.FloatField(null=False,blank=False,default=0.8)
    decay_rate=models.FloatField(null=False,blank=False,default=0.005)
    num_episodes=models.IntegerField(null=False,blank=False,default=1000)
    max_steps=models.IntegerField(null=False,blank=False,default=99)
    sum_rewards=models.IntegerField(null=False,blank=False,default=0)
    avg_rewards=models.FloatField(null=False,blank=False,default=0)
    table=models.JSONField(null=False,blank=False,default=defaultdict(lambda: np.zeros(500,6)))
    
    
    
    
# Create your models here.
