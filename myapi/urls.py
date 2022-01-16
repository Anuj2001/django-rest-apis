from django.urls import path,include
from .views import profile_create_api,profile_list_api,profile_update_api,profile_delete_api

urlpatterns=[
    path('auth/',include('rest_framework.urls'),name='Rest_url'),
    path('api/',profile_list_api.as_view(),name='Get_Profile'),
    path('api/create/',profile_create_api.as_view(),name='Create_Profile'),
    path('api/<int:pk>/',profile_update_api.as_view(),name='Update_Profile'),
    path('api/<int:pk>/delete',profile_delete_api.as_view(),name='Delete_Profile')
]