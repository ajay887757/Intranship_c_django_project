from androidapi.models import JobCode, ApplyEmpInfo,College,PassingYear, Stream_type
import bcrypt
from datetime import datetime

from androidapi.sendmail import send_acc_creation_mail

def checkJobcode(code1):
    try:
        code=JobCode.objects.filter(code=code1).values()
        return code
    except :
        pass

def checkempdetails(phone,email,whatsappnumber):
    response={}
    try:
        emailexist=ApplyEmpInfo.objects.filter(email=email).exists()
        if emailexist:
            response['mess']='ee' #email exist
            return response
        phonexist=ApplyEmpInfo.objects.filter(phoneno=phone).exists()   
        if phonexist:
            response['mess']='pe' #mobile number exist
            return response
        whexist=ApplyEmpInfo.objects.filter(whphoneno=whatsappnumber).exists()   
        if whexist:
            response['mess']='we' #whats app number exist number exist
            return response


        response['mess']='clear' #all data are distinct
        return response     
    except Exception as e:
        pass    

def crna(name,email,password,phonenumber,whatsappnumber,college_id,passing_year,branch_id,course_type,profile_name,gender_id,longitude,lattitude,state_id,dist_id,dob):
    response={}
    try:
        if branch_id!=None and branch_id=='':
            branch_id=None

        college=College.objects.get(id=college_id)
        py=PassingYear.objects.get(id=passing_year)
        stream_type=Stream_type.objects.get(id=course_type)
        hashed_password = bcrypt.hashpw(password.encode("utf8"), bcrypt.gensalt())
        passsword2= str(hashed_password).split("'")[1]
        ApplyEmpInfo.objects.create(longitude=longitude,lattitude=lattitude,gender=gender_id,name=name,phoneno=phonenumber,whphoneno=whatsappnumber,email=email,password=passsword2,course_type=stream_type,college=college,passing_year=py,branch=branch_id,photo=profile_name,created_at=datetime.now(),updated_at=datetime.now(),profile_status=0,fullsizephoto="",dist_id=dist_id,state_id=state_id,dob=dob)

        send_acc_creation_mail(name,email,password)
        response['mess']='done'
        return response
    except Exception as e:
        print(e)
        response['mess']='not'
        return response

def login(email,password):
    response={}
    try:
        emp=ApplyEmpInfo.objects.get(email=email,status=1)
        emp_password=emp.password
        if bcrypt.checkpw(password.encode("utf8"),emp_password.encode("utf8")):
            response["mess"] = "match"
            response["name"] = emp.name
            response["id"] = emp.id
        else:
            response["mess"] = "not"
        return response
    except Exception as e:
        response["mess"] = "not"
        return response    