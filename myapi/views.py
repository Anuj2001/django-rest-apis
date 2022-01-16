from rest_framework import generics
from rest_framework.response import Response
from .serializers import profile_serializer
from .models import Profile
from .custompermissions import CustomPermissions
# Create your apis here.


# To post some data:
class profile_create_api(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = profile_serializer
    permission_classes = [CustomPermissions]
# To get some data:
class profile_list_api(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = profile_serializer
    permission_classes = [CustomPermissions]
# To updata a record:
class profile_update_api(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = profile_serializer
    permission_classes = [CustomPermissions]
# To delete a record:
class profile_delete_api(generics.DestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = profile_serializer
    permission_classes = [CustomPermissions]



