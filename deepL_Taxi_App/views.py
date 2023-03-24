from django.shortcuts import render
from collections import deque
import sys
import math
import numpy as np
import time
import gym
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from django.http import JsonResponse
from collections import defaultdict
from rest_framework.views import APIView
from .models import Agent
from rest_framework.decorators import api_view
from .serializers import AgentSerializer
from rest_framework.views import APIView
import random
from rest_framework import generics
from rest_framework import permissions

@api_view(['GET'])
def affiche_agent(request):
    if request.method=='GET':
       agent=Agent.objects.filter(id=3)
       if  not agent: #or if len(students) ==0 or if bool(students): #if there is no student in the list 
            return Response(status=status.HTTP_204_NO_CONTENT)
       serializer= AgentSerializer(agent,many=True)
       return Response(serializer.data,status=status.HTTP_200_OK)
    return JsonResponse({"message":"The method is not allowed"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
 
class APIAgent(generics.UpdateAPIView):
    
 def main(self, request):
    agent=self.get(request)
    agent=Agent.objects.filter(id=3)
    serializer = AgentSerializer(agent, data=request.data, partial=True) # set partial=True to update a data partially
    # create Taxi environment
    env = gym.make('Taxi-v3')

    # initialize q-table
    state_size = env.observation_space.n
    action_size = env.action_space.n
    qtable = np.zeros((state_size, action_size))

    # hyperparameters
    serializer.data['learning_rate']  = 0.9
    serializer.data['discount_rate'] = 0.8
    serializer.data['epsilon'] = 1.0
    serializer.data['decay_rate'] = 0.005

    # training variables
    serializer.data['num_episodes'] = 1000
    serializer.data['max_steps'] = 99
    serializer.data['sum_all_rewards'] = 0
    # training
    for episode in range(agent.num_episodes):

        # reset the environment
        state = env.reset()
        done = False

        for s in range(agent.max_steps):

            # exploration-exploitation tradeoff
            if random.uniform(0,1) < agent.epsilon:
                # explore
                action = env.action_space.sample()
            else:
                # exploit
                action = np.argmax(qtable[state,:])

            # take action and observe reward
            new_state, reward, done, info = env.step(action)

            # Q-learning algorithm
            qtable[state,action] = qtable[state,action] + agent.learning_rate * (reward + agent.discount_rate * np.max(qtable[new_state,:])-qtable[state,action])

            # Update to our new state
            state = new_state

            # if done, finish episode
            if done == True:
                sum_all_rewards+=reward
                break

        # Decrease epsilon
        epsilon = np.exp(-agent.decay_rate*episode)

    print(f"Training completed over {agent.num_episodes} episodes")
    input("Press Enter to watch trained agent...")

    # watch trained agent
    state = env.reset()
    done = False
    rewards = 0

    for s in range(agent.max_steps):

        print(f"TRAINED AGENT")
        print("Step {}".format(s+1))

        action = np.argmax(qtable[state,:])
        new_state, reward, done, info = env.step(action)
        rewards += reward
        env.render()
        print(f"score: {rewards}")
        state = new_state
        if done == True:
            break

    env.close()
    avg_rewards=sum_all_rewards/agent.num_episodes
    serializer.data['avg_rewards']=avg_rewards
    if serializer.is_valid():
            serializer.save()
            return JsonResponse(code=201, data=serializer.data)
    return JsonResponse(code=400, data="wrong parameters")
    #agent=self.post(request)
   # return Response({'avg rewards':avg_rewards,'num of episods':agent.num_episodes})