from rest_framework import generics
from .serializers import profile_serializer
from .models import Profile
from .custompermissions import CustomPermissions
# Create your apis here.


# To Create or List data:
class profile_api(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = profile_serializer
    #permission_classes = [CustomPermissions]

# To get indivisual data or update or delete some data:
class single_profile_api(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = profile_serializer
    #permission_classes = [CustomPermissions]




