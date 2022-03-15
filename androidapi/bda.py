from cmath import exp
from datetime import datetime

import math, random
from operator import ge
from adminweb.models import SurveyLogin, Surveyinfo
from androidapi.models import Applied, ApplyEmpInfo, Voucher_Code
from androidapi.sendmail import send_enrollment_mail

def generateLoginpin() :
 
    # Declare a digits variable 
    # which stores all digits
    digits = "0123456789"
    OTP = ""
 
   # length of password can be changed
   # by changing value in range
    for i in range(4) :
        OTP += digits[math.floor(random.random() * 10)]
 
    return OTP
def Check_hr_code_voucher_code(hrcode,vouchercode):
    response={}
    try:
        if not ApplyEmpInfo.objects.filter(regid=hrcode,selected_job_profile=9,status=1,canhirestatus=1).exists():
            response['mess']='worng_hrcode'
        elif len(vouchercode) > 0 and not Voucher_Code.objects.filter(code=vouchercode,status=1).exists():
            response['mess']='worng_vouchercode'
        else:
            response['mess']='clear'
        return response    
    except Exception as e:
        response['mess']='network_error'
        return response  

def save_bda_payment(empid,txnid,amount,application_id,hrcode,voucher_code):
    response={}
    try:
        loginpin=generateLoginpin()
        applied=Applied.objects.filter(id=application_id)
        emp=ApplyEmpInfo.objects.get(id=empid)
        regid='CRTDBDA'+emp.name[0:2].upper()

        applied.update(Transactionid=txnid,amount_paid=amount,voucher_code=voucher_code,updated_at=datetime.now(),payment_date=datetime.now())
        if  len(voucher_code)>0:
            txnid=voucher_code
            Voucher_Code.objects.filter(code=voucher_code).update(status=0)
        surveylogindata=SurveyLogin.objects.using('CRTD-RC').create(survey_mobile=emp.phoneno,survey_email=emp.email,password="",survey_status=1,verified_status=0,survey_code_pin=loginpin,role=1,created_at=datetime.now(),updated_at=datetime.now(),work_status=0)
        count=''
        count=str(surveylogindata.survey_id) 
        regid=regid+count  
        surveylogindata.survey_registration_id=regid
        surveylogindata.save()

        empdata=ApplyEmpInfo.objects.filter(id=empid).update(loginpin=loginpin,referal_code=hrcode,regid=regid,selected_job_profile=applied[0].jobprofile)
        surveyinfodata=Surveyinfo.objects.using('CRTD-RC').create(voucher=txnid,survey_id=surveylogindata,survey_name=emp.name,survey_adhar_number="",survey_bankname="",survey_account_num="",survey_ifsc="",survey_branch="",survey_holder_name='',created_at=datetime.now(),updated_at=datetime.now())    
        send_enrollment_mail(regid,emp.email,emp.name)
        response['mess']='done'
        return response
    except Exception as e:
        response['mess']='not_done'
        return response        

def Change_loginpin(empid):
    response={}
    try:
        pin=generateLoginpin()
        empdata=ApplyEmpInfo.objects.filter(id=empid)
        empdata.update(loginpin=pin)
        SurveyLogin.objects.using('CRTD-RC').filter(survey_registration_id=empdata[0].regid).update(survey_code_pin=pin)
        response['mess']='done'
        return response    
    except Exception as e:
        response['mess']='not'
        return response  



