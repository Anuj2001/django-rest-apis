from django.urls import path,include
from .views import profile_api, single_profile_api
from rest_framework.authtoken.views import obtain_auth_token
from .custom_token import CustomAuthToken

urlpatterns=[
    # URL used for Session authentication
    #path('auth/',include('rest_framework.urls'),name='Rest_url'),

    #URL used for Token Authentication
    path('gettoken/',CustomAuthToken.as_view()),

    path('api/',profile_api.as_view()),
    path('api/<int:pk>/',single_profile_api.as_view()),
]