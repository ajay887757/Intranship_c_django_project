import io
from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from uritemplate import partial
from androidapi.Applied_info import appply, check_applied, get_applied, getallJobprofile
from androidapi.Basic_details import  Changeworkingstatus, GetAllStates, Save_device_token, add_hq, add_keyskills, addcontactus, emp_skills, get_bda_campus_type, get_districts, get_stream, getemp_edu, getempinfo, save_Aadhar_img, save_fullsizeimg, update_address, update_hq
from androidapi.HRdata import get_hiring_work_status
from androidapi.Tip import Getpaymentinfo, Tipappply, Tipcheckcode, Tipsave_payment, gettxttoken
from androidapi.bda import  Change_loginpin, Check_hr_code_voucher_code, save_bda_payment
from androidapi.get_clg_year import getallboard, getallcollege, getallpassingyear
from androidapi.models import ApplyEmpInfo
from androidapi.serializer import AppliedSerializer, BoardSerializer, District_serilizer, EmpEduSerializer, EmpinfoSerializer, JobprofileSerializer, PassingYearSerializer, State_serilizer, StreamSerializer, TipActivationcodeserilizer, college_codeSerializer, keySkillsSerializer
from androidapi.serializer import JobCodeSerializer

from androidapi.login_signup import checkJobcode, checkempdetails, crna, login
# Create your views here.


class check_jobcode(APIView):
    def post(self,request):
         try:
                code = request.data["code"]
                res=checkJobcode(code)
                result= JobCodeSerializer(res,many=True)
                return Response(result.data)
         except Exception as e:
             pass   
class Change_workingStatus(APIView):
    def post(self,request):
         try:
                res=Changeworkingstatus(request.data["empid"],request.data["status"])
                return Response(res)
         except Exception as e:
             pass   

class Get_clg(APIView):
    def post(self,request):
            try:
                res=getallcollege()
                result= college_codeSerializer(res,many=True)
                return Response(result.data)
            except Exception as e:
                return Response([])

class Get_passingyear(APIView):
    def post(self,request):
            try:
                res=getallpassingyear()
                result= PassingYearSerializer(res,many=True)
                return Response(result.data)
            except Exception as e:
                pass  

class Get_board(APIView):
    def post(self,request):
            try:
                res=getallboard()
                result= BoardSerializer(res,many=True)
                return Response(result.data)
            except Exception as e:
                pass  

class Get_Keyskills(APIView):
    def post(self,request):
            try:
                res=emp_skills(request.data['empid'])
                result= keySkillsSerializer(res,many=True)
                return Response(result.data)
            except Exception as e:
                pass  

class Save_Aadhar(APIView):
    def post(self,request):
            try:
                res=save_Aadhar_img(request.data['empid'],request.data['ab'],request.data['af'])
                return Response(res)
            except Exception as e:
                pass  

class Check_crna_data(APIView):
    def post(self,request):
        try:   
          res=checkempdetails(request.data['phonenumber'],request.data['email'],request.data['whatsappnumber'])
          return Response(res)
        except Exception as e:
            pass  

class Create_account(APIView):
    def post(self,request):
        try: 
          res=crna(request.data['name'],request.data['email'],request.data['password'],request.data['phonenumber'],request.data['whatsappnumber'],request.data['college_id'],request.data['passing_year'],request.data['branch_id'],request.data['course_type'],request.data['profile_name'],request.data['gender_id'],request.data['longitude'],request.data['lattitude'],request.data['state_id'],request.data['dist_id'],request.data['dob'])        
          return Response(res)
        except Exception as e:
            pass  

class Add_hq(APIView):  #add highest qualification 
    def post(self,request):
        try: 
          res=add_hq(request.data['empid'],request.data['hq_type'],request.data['board'],request.data['py'],request.data['sc_medium'],request.data['tm'])        
          return Response(res)
        except Exception as e:
            
            pass   

class Update_hq(APIView):  #update highest qualification
    def post(self,request):
        try: 
          res=update_hq(request.data['empid'],request.data['hq_type'],request.data['board'],request.data['py'],request.data['sc_medium'],request.data['tm'])        
          return Response(res)
        except Exception as e:
            
            pass   


class Update_Address(APIView):  #add highest qualification 
    def post(self,request):
        try: 
          res=update_address(request.data['empid'],request.data['paddress'],request.data['caddress'])        
          return Response(res)
        except Exception as e:

            pass   

class Add_Fullsizephoto(APIView):
    def post(self,request):
        try: 
          res=save_fullsizeimg(request.data['empid'],request.data['photo'])        
          return Response(res)
        except Exception as e:
           pass

class Add_contactus(APIView):
    def post(self,request):
        try: 
          res=addcontactus(request.data['name'],request.data['email'],request.data['phoneno'],request.data['message'])        
          return Response(res)
        except Exception as e:
           pass



class Add_skill(APIView):
    def post(self,request):
        try: 
          res=add_keyskills(request.data['empid'],request.data['keySkills'])        
          return Response(res)
        except Exception as e:
           pass
class Applied_login(APIView):
    def post(self,request):
        try: 
          res=login(request.data['email'],request.data['password'])        
          return Response(res)
        except Exception as e:            
            pass          
class Apply_empinfo(APIView):
    def post(self,request):
        try: 
          res=getempinfo(request.data['id']) 
          
          data=EmpinfoSerializer(res,many=True)
          return Response(data.data)
        except Exception as e:
            pass  
    def put(self,request):
        mssg={}
        try: 
          if ApplyEmpInfo.objects.filter(regid=request.data['referal_code'],selected_job_profile__id=9,status=1,canhirestatus=1).exists():
            Empdata=ApplyEmpInfo.objects.get(id=request.data['id'])          
            data=EmpinfoSerializer(Empdata,partial=True,data=request.data)
            if data.is_valid():
              data.save()
              mssg['mssg']='done'
            else:
              mssg['mssg']='notdone'
          else:
              mssg['mssg']='invalid hrcode'  
          return Response(mssg)
        except Exception as e:
          print(e)  
          mssg['mssg']='invalid hrcode'
          return Response(mssg)



class Apply_emp_edu(APIView):
    def post(self,request):
        try: 
          res=getemp_edu(request.data['id']) 
          data=EmpEduSerializer(res,many=True)       
          return Response(data.data)
        except Exception as e:
            pass  

#all Applied 
class Check_Applied(APIView):
    def post(self,request):
        try: 
          res=check_applied(request.data['empid']) 
          return Response(res)
        except Exception as e:
            pass  

class Apply_(APIView):
    def post(self,request):
        try: 
          res=appply(request.data['empid'],request.data['type'],request.data['subtype'],request.data['type_main'],request.data['jobcode']) 
          return Response(res)
        except Exception as e:
            pass  
class Jobprofile(APIView):
    def post(self,request):
        try: 
          res=getallJobprofile(request.data['type'],request.data['subtype']) 
          return Response(JobprofileSerializer(res,many=True).data)
        except Exception as e:
            pass          

class Get_applied(APIView):
    def post(self,request):
        try: 
          res=get_applied(request.data['empid']) 
          return Response(AppliedSerializer(res,many=True).data)
        except Exception as e:
            pass 
#tip code start
class TipCheckCode(APIView):
    def post(self,request):
        try: 
          res=Tipcheckcode(request.data['code']) 
          return Response(TipActivationcodeserilizer(res,many=True).data)
        except Exception as e:
            pass 

class Tip_tranx_token(APIView):
    def post(self,request):
        try: 
          res=gettxttoken(request.data['orderid'],request.data['mobile'],request.data['price']) 
          return Response(res)
        except Exception as e:
            pass 

class TipApply_(APIView):
    def post(self,request):
        try: 
          res=Tipappply(request.data['empid'],request.data['type'],request.data['subtype'],request.data['type_main'],request.data['txnid']) 
          return Response(res)
        except Exception as e:
            pass

class Tipsaverepayment(APIView):
    def post(self,request):
        try: 
          res=Tipsave_payment(request.data['empid'],request.data['amount'],request.data['txnid']) 
          return Response(res)
        except Exception as e:
            pass          
class Tippaymentinfo(APIView):
    def post(self,request):
        try: 
          res=Getpaymentinfo(request.data['empid']) 

          return Response(res)
        except Exception as e:
            pass          
#HR DASHBOARD DATA

class GET_HIRING_work_status(APIView):
    def post(self,request):
        try: 
          res=get_hiring_work_status(request.data['empid']) 

          return Response(res)
        except Exception as e:
            pass            

class GET_ALL_STATE(APIView):
    def post(self,request):
        try: 
          res=GetAllStates()
          return Response(State_serilizer(res,many=True).data)
        except Exception as e:
            return Response([])
class GET_DISTRICT(APIView):
    def post(self,request):
        try: 
          res=get_districts(request.data['state_id'])
          return Response(District_serilizer(res,many=True).data)
        except Exception as e:
            return Response([])
class CHECK_HR_CODE_VOUCHER(APIView):
    def post(self,request):
        try: 
          res=Check_hr_code_voucher_code(request.data['hrcode'],request.data['voucher'])
          return Response(res)
        except Exception as e:
            pass

class SAVE_BDA_PAYMENT(APIView):
    def post(self,request):
        try: 
          res=save_bda_payment(request.data['empid'],request.data['txnid'],request.data['amount'],request.data['application_id'],request.data['hrcode'],request.data['voucher'])
          return Response(res)
        except Exception as e:
            pass                                                   

class SAVE_DEVICE_TOKEN(APIView):
    def post(self,request):
        try: 
          res=Save_device_token(request.data['empid'],request.data['device_token'])
          return Response([])
        except Exception as e:
            pass      

class GET_STREAM(APIView):
    def post(self,request):
        try: 
          res=get_stream()
          return Response(StreamSerializer(res,many=True).data)
        except Exception as e:
            pass
class CHANGE_LOGINPIN(APIView):
    def post(self,request):
        try: 
          res=Change_loginpin(request.data['empid'])
          return Response(res)
        except Exception as e:
            pass     

class GET_BDA_CAMPUS_TYPE(APIView):
  def get(self,request):
    try:
      return Response(get_bda_campus_type())
    except Exception as e:
      pass