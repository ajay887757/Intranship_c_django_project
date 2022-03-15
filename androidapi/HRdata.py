from datetime import *
from tkinter.messagebox import NO
from adminweb.models import Surveyinfo

from androidapi.models import ApplyEmpInfo, EmpReport, HrTarget

def get_hiring_work_status(empid):
    response={}
    try:
        today_min = datetime.combine(date.today(), time.min)
        today_max = datetime.combine(date.today(), time.max)
        emp=ApplyEmpInfo.objects.get(id=empid)
        try:
            report=EmpReport.objects.get(created_at__range=(today_min,today_max),emp__id=empid)
            response['work_status']= report.workingstatus
            response['date']= report.updated_at
        except Exception as e:
             response['work_status']= None

        Hrtarget=HrTarget.objects.filter(month=date.today().month,emp__id=empid)
        totalhiring=ApplyEmpInfo.objects.filter(referal_code=emp.regid).count()
        response['totalhiring']=totalhiring
        if  Hrtarget!=None and len(Hrtarget)>0:
            response['target']=Hrtarget[0].target
        else:
            response['target']=0
        return response


    except Exception as e:
        response['work_status']=None
        response['totalhiring']=0
        response['target']=0
        return response
        