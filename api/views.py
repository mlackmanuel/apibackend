
from api.models import Contact
from .serializers import ContactSerializer

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

# Create your views here.


class ContactAPIView(generics.ListCreateAPIView):
    serializer_class=ContactSerializer
    permission_classes=[ AllowAny]
    queryset=Contact.objects.all()
    
    # def list(self,request):
    #     queryset=self.get_queryset()
    #     serializer=ContactSerializer(queryset,many=True)
    #     return Response(serializer.data)
    
    