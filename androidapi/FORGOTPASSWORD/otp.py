from androidapi.models import ApplyEmpInfo
import requests
import json
from django.utils import timezone
from django.db.models import F
from rest_framework.views import APIView
from rest_framework.response import Response

from datetime import datetime,timedelta

# import library
import math, random

# function to generate OTP
def generateOTP() :

	# Declare a digits variable
	# which stores all digits
	digits = "123456789"
	OTP = ""

# length of password can be changed
# by changing value in range
	for i in range(4) :
		OTP += digits[math.floor(random.random() * 10)]

	return OTP

class Send_mail_otp(APIView):
   def get(self,request):
       Response("")
   def post(self,request):
       try:
           return Response (self.sendotp_emp(request.data['mail']))
       except Exception as e:
           print(e)
           pass     
   def sendotp_emp(self,mail):
    response={}
    otp=generateOTP()
    try:
        data={}
        data['mail']=mail
        data['otp']=otp
        if ApplyEmpInfo.objects.filter(email=mail).exists():
            data['name']=ApplyEmpInfo.objects.get(email=mail).name
            postdata= json.dumps(data)
            ApplyEmpInfo.objects.filter(email=mail).update(otp_recovery=otp,otp_recovery_date=datetime.now())
            result = requests.post('http://crtd.in/sendotpmail.php', data =postdata , headers = {"Content-type": "application/json"}).json()
            if result!=None and  result=='sent':
                response['mess']='001' #mail sent
            else:
                response['mess']='504' #mail not sent  

        else:
            response['mess']='404' #not found
        return response
    except Exception as e:
        print(e)
        response['mess']='404' #not found
        return response

class Matchotp(APIView):
    def get(self,request):
       Response("")
    def post(self,request):
       try:
           return Response (self.matchotp_emp(request.data['otp'],request.data['mail']))
       except Exception as e:
           print(e)
           pass 
    def matchotp_emp(otp,mail):
        response={}
        try:
            surveyor=ApplyEmpInfo.objects.filter(email=mail,otp_recovery=otp).annotate(
                diff= datetime.now()- F('otp_recovery_date')
            ).values('diff')
            timediff=surveyor[0]['diff']
            if timediff.total_seconds()<300:
                response['mess']='001'
            else:
                response['mess']='404'   

            return response
        except Exception as e:
            response['mess']='404'
            return response
