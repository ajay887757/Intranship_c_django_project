from this import d
from grpc import Status
from rest_framework import response
from androidapi.models import ApplyEmpInfo, Contactus, EmpReport, EmpkeySkill, Job_profile,PassingYear,Board,EmpEducations, Stream_type
from datetime import datetime
from adminweb.models import District, State

def getempinfo(empid):
    
    # try:
    try:
        emp=ApplyEmpInfo.objects.filter(id=empid)
        return emp
    except Exception as e:
        pass   
 
def getemp_edu(empid):  #employee education 
    # try:
    try:
        emp=EmpEducations.objects.filter(emp__id=empid).order_by("-hq_type")
        return emp
    except Exception as e:
        pass   
 

def update_address(empid,paddress,caddress):
    try:
        response={}
        ApplyEmpInfo.objects.filter(id=empid).update(paddress=paddress,caddress=caddress)
        response['mess']='done'
        return response
    except Exception as e:
        response['mess']='notdone'
        return response
         
def add_keyskills(empid,skills):
    response={}
    try:
        EmpkeySkill.objects.filter(emp__id=empid).delete()
        emp=ApplyEmpInfo.objects.get(id=empid)
        for skill in skills:
            EmpkeySkill.objects.create(emp=emp,title=skill["title"],created_at=datetime.now())
        response['mess']='done'       
        return response
    except Exception as e:
        response['mess']='not'  
        return response

def emp_skills(id):
      # try:
    try:
        keyskill=EmpkeySkill.objects.filter(emp__id=id)
        return keyskill
    except Exception as e:
        pass


def add_hq(empid,hq_type,board,py,sc_medium,tm):
    response={}
    try:

     emp=ApplyEmpInfo.objects.get(id=empid)
     board_d=Board.objects.get(id=board)
     py_d=PassingYear.objects.get(id=py)
     EmpEducations.objects.create(hq_type=hq_type,school_medium=sc_medium,total_marks=tm,board=board_d,emp=emp,py=py_d,  created_at=datetime.now(),updated_at=datetime.now())
     response['mess']='done'
     return response  
    except Exception as e:
        response['mess']='exp'
        return response

def save_Aadhar_img(empid,ab,af):
    try:
        response={}
        ApplyEmpInfo.objects.filter(id=empid).update(Aadhar_front_img=af,Aadhar_back_img=ab)
        response['mess']='done'
        return response
    except Exception as e:
        response['mess']='not'
        return response
        
def save_fullsizeimg(empid,fullsizeimg):
    try:
        response={}
        ApplyEmpInfo.objects.filter(id=empid).update(fullsizephoto=fullsizeimg)
        response['mess']='done'
        return response
    except Exception as e:
        response['mess']='not'
        return response
        



def update_hq(empid,hq_type,board,py,sc_medium,tm):
    response={}
    try:

     emp=ApplyEmpInfo.objects.get(id=empid)
     board_d=Board.objects.get(id=board)
     py_d=PassingYear.objects.get(id=py)
     EmpEducations.objects.filter(emp__id=empid).update(hq_type=hq_type,school_medium=sc_medium,total_marks=tm,board=board_d,emp=emp,py=py_d,  created_at=datetime.now(),updated_at=datetime.now())
     response['mess']='done'
     return response  
    except Exception as e:
        response['mess']='exp'
        return response        



#contact us
def addcontactus(name,email,phonenumber,message):
    response={}
    try:
        Contactus.objects.create(name=name,email=email,phoneno=phonenumber,message=message)
        response['mess']='done'
        return response
    except Exception as  e:
        response['mess']='notdone'
        return response    

def Changeworkingstatus(empid,status):
    response={}
    try:
        emp=ApplyEmpInfo.objects.get(id=empid)
        report=EmpReport.objects.filter(emp__id=empid)
        if report.exists():
            report.update(workingstatus=status,updated_at=datetime.now())
        else:
            EmpReport.objects.create(emp=emp,workingstatus=1,)    
        response['mess']='done'
        response['date']=datetime.now()
        return response
    except Exception as e:
        response['mess']='not'
        return response

def GetAllStates():
    try:
        return State.objects.using("CRTD-RC").all()
    except Exception as e:
        pass
def get_districts(state_id):
    try:
        return District.objects.using("CRTD-RC").filter(state_id=state_id)
    except Exception as e:
        pass 
def get_stream():
    try:
        return Stream_type.objects.filter(status=1)
    except Exception as e:
        pass         
def Save_device_token(empid,devicetoken):
    response={}
    try:
        ApplyEmpInfo.objects.filter(id=empid).update(device_token=devicetoken)
    except Exception as e:
        pass    

def get_bda_campus_type():
    try:
        return Job_profile.objects.get(id=17).hiretype
    except Exception as e:
        pass