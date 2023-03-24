from django.urls import include,path
from rest_framework import routers
from . import views
from .viewset import AgentViewSet
from . import views
#urls using ModelViewSet
# from university_app.viewsets import AddressViewSet, GroupViewSet, StudentViewSet
 #get the default router object defined in rest_framework
# #add router for each viewset (StudentViewest, GroupViewSet, AddressViewSet) to the router object

# #each time we use the path '/students' in the url, 
# #the StudentViewSet will be called
# #the prefix r is used to indicate that the string is a raw string (not interpret the backslash as an escape character)
# router.register(r'groups',GroupViewSet)
# router.register(r'addresses',AddressViewSet)

# #add the router to the urlpatterns

router=routers.DefaultRouter()
router.register(r'Agent',AgentViewSet) 
"""
urlpatterns = [
     path('', include(router.urls)),]

"""
urlpatterns = [
     path(r"afficher", views.affiche_agent),
     path(r"main",views.APIAgent.as_view()),
]  
