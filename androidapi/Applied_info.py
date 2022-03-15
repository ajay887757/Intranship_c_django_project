from androidapi.models import Applied, ApplyEmpInfo, Job_profile, JobCode
from datetime import datetime
from django.db.models import Q

#404 not found
#200  found
#500 exception occured
def check_applied(empid):
    response={}
    try:
        #check employee already applied and the application is pending or selected or selected for interview 
        if not Applied.objects.filter(emp__id=empid).filter(Q(status=1)|Q(status=3)|Q(status=4)|Q(status=7)).exists():
            response['mess']='404'
        else:
            response['mess']='200'
        return response
    except Exception as e:
        response['mess']='500'
        return response

def getallJobprofile(type,subtype):
    try:
        jp=Job_profile.objects.filter(type=type,sub_type=subtype, status=1)
        return jp
    except Exception as e :
        pass

def get_applied(empid):
    try:
        return Applied.objects.filter(emp__id=empid).order_by("-updated_at")
    except Exception as e:
        pass


def appply(empid,apply_type,jobprofiletype,type,jobcode):
    response={}
    try:
        if not Applied.objects.filter(emp__id=empid).filter(Q(status=1)|Q(status=3)|Q(status=4)|Q(status=7)).exists():
            emp=ApplyEmpInfo.objects.get(id=empid)
            jp=Job_profile.objects.get(id=jobprofiletype)
            jobcode1=JobCode.objects.get(code=jobcode)
            Applied.objects.create(jobcode=jobcode1, emp=emp,apply_type=apply_type,type=type, status=1,jobprofile=jp, created_at=datetime.now(),updated_at=datetime.now())
            response['mess']='100' #done
        else:
            response['mess']='200'
        return response
    except Exception as e:
        response['mess']='500'
        return response