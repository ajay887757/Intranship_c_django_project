from rest_framework import response
from androidapi.models import ApplyEmpInfo
import bcrypt
from django.utils import timezone
from django.db.models import F
from rest_framework.views import APIView
from rest_framework.response import Response

class Change_password(APIView):
    def get(self,request):
        return Response("")
    def post(self,request):
        response={}
        try:
            hashed_password = bcrypt.hashpw(request.data['password'].encode("utf8"), bcrypt.gensalt())
            passsword2= str(hashed_password).split("'")[1]
            emp=ApplyEmpInfo.objects.filter(email=request.data['email']).update(passsword=passsword2)
            response['mess']='001'
            return response      
        except Exception as e:
            response['mess']='404'
            return response    