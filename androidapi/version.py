from androidapi.models import Appversion
from rest_framework.views import APIView
from rest_framework.response import Response

from androidapi.serializer import AppversionSerializer

class Get_appversion(APIView):
    def post(self,request):
        try:
            version=Appversion.objects.order_by('-id')[0:1]
            return Response(AppversionSerializer(version,many=True).data)
        except  Exception as e:
            return Response([])
