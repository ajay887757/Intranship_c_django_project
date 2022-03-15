import calendar
from time import sleep
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse

from androidapi.sendmail import send_status_change_mail
from .Bda import get_bda_data
import bcrypt
from datetime import *
from django.utils import timezone

from androidapi.models import Adminlogins,Applied, JobCode,TIPActivationCode, ApplyEmpInfo, College, Job_profile,PassingYear,EmpEducations,EmpkeySkill, TipCampusexecutive, Tippayment
from androidapi.sendnotification import sendpushnotification
from adminweb.models import District, State
# Create your views here.
def Login(request):
    try:
        result = request.session['ADMIN']
        return redirect("admin-dashboard")
    except Exception as e:
        return render(request,'admin_temp/Login.html')

def Logout(request):
    request.session.flush()


def CheckAdminLogin(request):
    

    try:
        emailid = request.POST['emailid']
        
        password = request.POST['password']
        admin=Adminlogins.objects.get(email=emailid, user_status=1)
        # Adminlogins.ob
        if bcrypt.checkpw(password.encode("utf8"), admin.password.encode("utf8")):
            request.session['ADMIN']=admin.id
            return redirect('admin-dashboard')
        else:
            return render(request, "admin_temp/Login.html", { 'msg': 'Invalid Userid or Password'})

    except Exception as e:
          Logout(request) 
          return render(request, "admin_temp/Login.html", {'msg': 'Server Error'})

def get_month_max(year,month):
    last_day=calendar.monthrange(year, month)[1]
    return datetime(year,month,last_day,23,59,59)


def Admindashboard(request):
    today_min = datetime.combine(date.today(), time.min)
    today_max = datetime.combine(date.today(), time.max)
    if(request.POST.get('cmonth')!=None):
        month=int(request.POST.get('cmonth'))
    elif(request.POST.get('cmonth')==None):
        month=timezone.now().month
  
    if(request.POST.get('cyear')!=None):
        year=int(request.POST.get('cyear'))
        
    elif(request.POST.get('cyear')==None):
        year=timezone.now().year
        

    month_max=get_month_max(year,month)
    month_min=(timezone.now().replace(day=1).replace(month=int(month)).replace(year=int(year)) )
 
    try:
        result = request.session['ADMIN']
        total_internship=Applied.objects.filter( type=1 ).filter(created_at__range=(month_min,month_max) )
        today_internship=Applied.objects.filter( type=1 ).filter(created_at__range=(today_min, today_max)).count()
        total_jobs=Applied.objects.filter( type=2 ).filter(created_at__range=(month_min,month_max) )
        today_jobs=Applied.objects.filter( type=2 ).filter(created_at__range=(today_min, today_max)).count()
        total_tip=Applied.objects.filter( type=3).filter(created_at__range=(month_min,month_max) )
        today_tip=Applied.objects.filter( type=3 ).filter(created_at__range=(today_min, today_max)).count()
        todayacccreate=ApplyEmpInfo.objects.filter(created_at__range=(today_min, today_max)).count() #today account created

        totalacccreate=ApplyEmpInfo.objects.filter(created_at__range=(month_min, month_max)).count() #total acccount create
        not_applied=ApplyEmpInfo.objects.exclude(id__in=(Applied.objects.filter(created_at__range=(month_min,month_max)))).filter(created_at__range=(today_min, today_max)).count()

        totalapplied=total_internship.count()+total_jobs.count()+total_tip.count()
        totalselected=total_internship.filter(status=3).count()+total_jobs.filter(status=3).count()+total_tip.filter(status=3).count()
        totalrejected=total_internship.filter(status=2).count()+total_jobs.filter(status=2).count()+total_tip.filter(status=2).count()
        Alltipcampusexe=TipCampusexecutive.objects.all().count()
        totalapplied_bda_off,totalselected_bda_off,totalrejected_bda_off,total_enrollment_expired_bda_off,enrollmentpending_bda_off,enrollmenthold_bda_off,selected_for_enrollment_off,interview_going_on_bda_off=get_bda_data(month_min,month_max,today_min,today_max,'all',1)        
        totalapplied_bda_on,totalselected_bda_on,totalrejected_bda_on,total_enrollment_expired_bda_on,enrollmentpending_bda_on,enrollmenthold_bda_on,selected_for_enrollment_on,interview_going_on_bda_on=get_bda_data(month_min,month_max,today_min,today_max,'all',2)        


        param={
            "totalapplied_bda_off":totalapplied_bda_off,
            "totalselected_bda_off":totalselected_bda_off,
            "totalrejected_bda_off":totalrejected_bda_off,
            "enrollmentpending_bda_off":enrollmentpending_bda_off,
            "enrollmenthold_bda_off":enrollmenthold_bda_off,
            "selected_for_enrollment_off":selected_for_enrollment_off,
            "total_enrollment_expired_bda_off":total_enrollment_expired_bda_off,
            "interview_going_on_bda_off":interview_going_on_bda_off,
            "interview_going_on_bda_on":interview_going_on_bda_on,

            "totalapplied_bda_on":totalapplied_bda_on,
            "totalselected_bda_on":totalselected_bda_on,
            "totalrejected_bda_on":totalrejected_bda_on,
            "enrollmentpending_bda_on":enrollmentpending_bda_on,
            "enrollmenthold_bda_on":enrollmenthold_bda_on,
            "selected_for_enrollment_on":selected_for_enrollment_on,
            "total_enrollment_expired_bda_on":total_enrollment_expired_bda_on,

            "totalrejected":totalrejected,
            "totalapplied":totalapplied,
            "totalselected":totalselected,
            "not_applied":not_applied,
            "todayacccreate":todayacccreate,
            "totalacccreate":totalacccreate,
            'year':year,
            'month':month,
            'today_jobs':today_jobs,
            'today_internship':today_internship,
            'today_tip':today_tip,
            'total_jobs':total_jobs.count(),
            'total_internship':total_internship.count(),
            'total_tip':total_tip.count(),
            "Alltipcampusexe":Alltipcampusexe
            }
        return render(request, "admin_temp/Dashboard.html",param)
    except  Exception as e:
        Logout(request) 
        return redirect('admin-login')

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def getAppliedCount(type,applytype,status,subtype,time_min,time_max):
    #subtype 1:total 2:today
    try:
        data=Applied.objects.filter( type=type ,apply_type=applytype,status=status).filter(updated_at__range=(time_min, time_max) )
        return  data
    except Exception as e:
        return  []

def InternshipView(request,id):
 
    try:
        today_min = datetime.combine(date.today(), time.min)
        today_max = datetime.combine(date.today(), time.max)
        if(request.POST.get('cmonth')!=None):
            month=int(request.POST.get('cmonth'))
        elif(request.POST.get('cmonth')==None):
            month=timezone.now().month

        if(request.POST.get('cyear')!=None):
            year=int(request.POST.get('cyear'))
        
        elif(request.POST.get('cyear')==None):
            year=datetime.now().year
        month_min=(datetime.now().replace(day=1).replace(month=int(month)).replace(year=int(year)))
        month_max=get_month_max(year,month)

        result = request.session['ADMIN']
        if(id==1): #internship selected
            
            total_tech_interview=getAppliedCount(1,1,3,1,month_min,month_max).count()
            today_tech_interview=getAppliedCount(1,1,3,2,today_min,today_max).count()
            total_hr_interview=getAppliedCount(1,2,3,1,month_min,month_max).count()
            today_hr_interview=getAppliedCount(1,2,3,2,today_min,today_max).count()
            return render(request,'admin_temp/Internship.html',{'year':year,'month':month,'id':str(id),'text':'Selected For Internship','total_tech_interview':total_tech_interview,'today_tech_interview':today_tech_interview,'total_hr_interview':total_hr_interview,'today_hr_interview':today_hr_interview})        
        elif(id==2): #internship selected for interview
            total_tech_interview=getAppliedCount(1,1,4,1,month_min,month_max).count()
            today_tech_interview=getAppliedCount(1,1,4,2,today_min,today_max).count()
            total_hr_interview=getAppliedCount(1,2,4,1,month_min,month_max).count()
            today_hr_interview=getAppliedCount(1,2,4,2,today_min,today_max).count()
            return render(request,'admin_temp/Internship.html',{'year':year,'month':month,'id':str(id),'text':'Selected For an interview for Internship ','total_tech_interview':total_tech_interview,'today_tech_interview':today_tech_interview,'total_hr_interview':total_hr_interview,'today_hr_interview':today_hr_interview})        
        elif(id==3): #internship rejected
            total_tech_interview=getAppliedCount(1,1,2,1,month_min,month_max).count()
            today_tech_interview=getAppliedCount(1,1,2,2,today_min,today_max).count()
            total_hr_interview=getAppliedCount(1,2,2,1,month_min,month_max).count()
            today_hr_interview=getAppliedCount(1,2,2,2,today_min,today_max).count()
            return render(request,'admin_temp/Internship.html',{'year':year,'month':month,'id':str(id),'text':'Rejected For Internship','total_tech_interview':total_tech_interview,'today_tech_interview':today_tech_interview,'total_hr_interview':total_hr_interview,'today_hr_interview':today_hr_interview})        

        elif(id==4): #internshp applied
            total_tech_interview=getAppliedCount(1,1,1,1,month_min,month_max).count()
            today_tech_interview=getAppliedCount(1,1,1,2,today_min,today_max).count()
            total_hr_interview=getAppliedCount(1,2,1,1,month_min,month_max).count()
            today_hr_interview=getAppliedCount(1,2,1,2,today_min,today_max).count()
            return render(request,'admin_temp/Internship.html',{'year':year,'month':month,'id':str(id),'text':'Applied For Internship','total_tech_interview':total_tech_interview,'today_tech_interview':today_tech_interview,'total_hr_interview':total_hr_interview,'today_hr_interview':today_hr_interview })        
    
    except Exception as e:
        Logout(request) 
        return redirect('admin-login')



def getcandidatelistdata(type,applytype,status,time_min,time_max):
    #subtype 1:total 2:today
    try:    
        data=Applied.objects.filter( type=type ,apply_type=applytype,status=status).filter(updated_at__range=(time_min,time_max) )
        return  data
    except Exception as e:
        return  []

def getalldata(type,time_min,time_max):
    try:    
        data=Applied.objects.filter( type=type ).filter(created_at__range=(time_min,time_max) )
        return  data
    except Exception as e:
        return  []
def candidatelist(request,id,id1,id2,id3,title):
    
    today_min = datetime.combine(date.today(), time.min)
    today_max = datetime.combine(date.today(), time.max)
    month=id2
    year=id3
    data=[]    

    month_min=(datetime.now().replace(day=1).replace(month=int(month)).replace(year=int(year)))
    month_max=get_month_max(year,month)

   
    try:
        if(id==1): #internship selected
            if(id1=='total_tech'):
                data=getcandidatelistdata(1,1,3,month_min,month_max)
            elif(id1=='today_tech'):
                data=getcandidatelistdata(1,1,3,today_min,today_max)
            elif(id1=='total_hr'):
                data=getcandidatelistdata(1,2,3,month_min,month_max)
            elif(id1=='today_hr'):
                data=getcandidatelistdata(1,2,3,today_min,today_max)
        elif(id==2): #internship selected for interview
            if(id1=='total_tech'):
                data=getcandidatelistdata(1,1,4,month_min,month_max)
            elif(id1=='today_tech'):
                data=getcandidatelistdata(1,1,4,today_min,today_max)
            elif(id1=='total_hr'):
                data=getcandidatelistdata(1,2,4,month_min,month_max)
            elif(id1=='today_hr'):
                data=getcandidatelistdata(1,2,4,today_min,today_max)
        elif(id==3):  #nternship rejected
            if(id1=='total_tech'):
                data=getcandidatelistdata(1,1,2,month_min,month_max)
            elif(id1=='today_tech'):
                data=getcandidatelistdata(1,1,2,today_min,today_max)
            elif(id1=='total_hr'):
                data=getcandidatelistdata(1,2,2,month_min,month_max)
            elif(id1=='today_hr'):
                data=getcandidatelistdata(1,2,2,today_min,today_max)
        elif(id==4): #internship  applied
            if(id1=='total_tech'):
                data=getcandidatelistdata(1,1,1,month_min,month_max)
            elif(id1=='today_tech'):
                data=getcandidatelistdata(1,1,1,today_min,today_max)
            elif(id1=='total_hr'):
                data=getcandidatelistdata(1,2,1,month_min,month_max)
            elif(id1=='today_hr'):
                data=getcandidatelistdata(1,2,1,today_min,today_max)
        elif(id==5):#internship all data
            if(id1=='today'):
                data=getalldata(1,today_min,today_max)
            elif(id1=='total'):
                data=getalldata(1,month_min,month_max)
        elif(id==6):#job all data
            if(id1=='today'):
                data=getalldata(2,today_min,today_max)
            elif(id1=='total'):
                data=getalldata(2,month_min,month_max)
        elif(id==7):#tip all data
            if(id1=='today'):
                data=getalldata(3,today_min,today_max)
            elif(id1=='total'):
                data=getalldata(3,month_min,month_max)
                     
        return render(request,'admin_temp/candidatelist.html',{'res':data,'title':title})        
    except Exception as e:
        Logout(request) 
        return redirect('admin-login')
   
def Drawer(request,id):
    try:
        
        result = request.session['ADMIN']
        if(id==1): #dashboard
            return redirect('admin-dashboard')          
        if(id==2): #activation code
                t=TIPActivationCode.objects.all()      
                return render(request, "admin_temp/EmployeeActivationCode.html",{'t':t})
        if(id==3): #passing year
                t=PassingYear.objects.all()      
                return render(request, "admin_temp/PassingYear.html",{'t':t})
        if(id==4): #college list
                t=College.objects.all()      
                return render(request, "admin_temp/collegelist.html",{'t':t})
        if(id==5): #Job code list
                t=JobCode.objects.all()      
                return render(request, "admin_temp/Jobcode.html",{'t':t})        
    except Exception as e:
        Logout(request) 
        return redirect('admin-login')          


def Addcollege(request):
    
    try:
        result = request.session['ADMIN']
        if is_ajax(request=request) and request.method == "POST":
            clgname = request.POST.get('addcollegename',None)
            r=College.objects.all().values("name")
            for i in r:
                if(i['name']==clgname):
                    return JsonResponse({"error": "Already exists"}, status=400)
                   
            t=College.objects.create(name=clgname,status=1,created_at=timezone.now())   
            

            return JsonResponse({"status": "done"}, status=200)

    # some error occured
        return JsonResponse({"error": "Status not upadated"}, status=400)
    except  Exception as e:
           return JsonResponse({"error": "Status not upadated "}, status=400)


def Editclgname(request):
    try:
        result = request.session['ADMIN']
        if is_ajax(request=request) and request.method == "POST":
            clg = request.POST.get('clgname',None)
            cid = request.POST.get('cid',None)
            r=College.objects.all().values("name")
            for i in r:
                if(i['name']==clg):
                    return JsonResponse({"error": "Already exists"}, status=400)
            College.objects.filter(id=cid).update(name=clg)
           
            

            return JsonResponse({"status": "done"}, status=200)

    # some error occured
        return JsonResponse({"error": "Status not upadated"}, status=400)
    except  Exception as e:
        
            return JsonResponse({"error": "Status not upadated "}, status=400)

def Deleteclg(request):
    try:
        result = request.session['ADMIN']
        if is_ajax(request=request) and request.method == "POST":
            cid = request.POST.get('deletecid',None)
            College.objects.filter(id=cid).delete()
            return JsonResponse({"status": "done"}, status=200)
    # some error occured
        return JsonResponse({"error": "Status not upadated"}, status=400)
    except  Exception as e:
            return JsonResponse({"error": "Status not upadated "}, status=400)
 
def update_clgstatus(request):
    try:
        result = request.session['ADMIN']
        if is_ajax(request=request) and request.method == "POST":
            status=None
            if request.POST['data']=="0":
                status=1
            else:
                status=0
            College.objects.filter(id=request.POST['regid']).update(status=status)       
            return JsonResponse({"status": "done"}, status=200)

        return JsonResponse({"error": "Status not upadated"}, status=400)
    except  Exception as e:
            return JsonResponse({"error": "Status not upadated "}, status=400)


def Addactivationcode(request):
    
    try:
        result = request.session['ADMIN']
        if is_ajax(request=request) and request.method == "POST":
            code = request.POST.get('addcode',None)
            date = request.POST.get('adddate',None)
            r=TIPActivationCode.objects.all().values("code")
            for i in r:
                if(i['code']==code):
                    return JsonResponse({"error": "Already exists"}, status=400)
            t=TIPActivationCode.objects.create(code=code,valid_date=date,created_at=timezone.now(),updated_at=timezone.now())   
            # t.save()
             
            

            return JsonResponse({"status": "done"}, status=200)

    # some error occured
        return JsonResponse({"error": "Status not upadated"}, status=400)
    except  Exception as e:
            return JsonResponse({"error": "Status not upadated "}, status=400)
 
       

def Editactivationcode(request):
    try:
        result = request.session['ADMIN']
        if is_ajax(request=request) and request.method == "POST":

            date = request.POST.get('validdate',None)
            aid = request.POST.get('activationid',None)
            
           

            if(date):
                TIPActivationCode.objects.filter(id=aid).update(valid_date=date,updated_at=timezone.now())
           
            
            
            return JsonResponse({"status": "done"}, status=200)

    # some error occured
        return JsonResponse({"error": "Status not upadated"}, status=400)
    except  Exception as e:
            return JsonResponse({"error": "Status not upadated "}, status=400)
 
      
def Deleteactivationcode(request):
    try:
        result = request.session['ADMIN']
        if is_ajax(request=request) and request.method == "POST":
            aid = request.POST.get('deleteaid',None)
            TIPActivationCode.objects.filter(id=aid).delete()
            
           
            

            return JsonResponse({"status": "done"}, status=200)

    # some error occured
        return JsonResponse({"error": "Status not upadated"}, status=400)
    except  Exception as e:
        
            return JsonResponse({"error": "Status not upadated "}, status=400)
 

def Addjobcode(request):
    
    try:
        result = request.session['ADMIN']
        if is_ajax(request=request) and request.method == "POST":
            code = request.POST.get('addcode',None)
            date = request.POST.get('adddate',None)
            r=JobCode.objects.all().values("code")
            for i in r:
                if(i['code']==code):
                    return JsonResponse({"error": "Already exists"}, status=400)
            t=JobCode.objects.create(code=code,valid_date=date,created_at=timezone.now(),updated_at=timezone.now())   
            # t.save()
             
            

            return JsonResponse({"status": "done"}, status=200)

    # some error occured
        return JsonResponse({"error": "Status not upadated"}, status=400)
    except  Exception as e:
            return JsonResponse({"error": "Status not upadated "}, status=400)
 
       

def Editjobcode(request):
    try:
        result = request.session['ADMIN']
        if is_ajax(request=request) and request.method == "POST":

            date = request.POST.get('validdate',None)
            aid = request.POST.get('activationid',None)
            
           

            if(date):
                JobCode.objects.filter(id=aid).update(valid_date=date,updated_at=timezone.now())
           
            
            
            return JsonResponse({"status": "done"}, status=200)

    # some error occured
        return JsonResponse({"error": "Status not upadated"}, status=400)
    except  Exception as e:
            return JsonResponse({"error": "Status not upadated "}, status=400)
 
      


def AddPassingYear(request):
    
    try:
        result = request.session['ADMIN']
        if is_ajax(request=request) and request.method == "POST":
            code = int(request.POST.get('addcode',None))
            r=PassingYear.objects.all().values("name")
            for i in r:
                if(i['name']==code):
                    return JsonResponse({"error": "Already exists"}, status=400)
            t=PassingYear.objects.create(name=code,created_at=timezone.now())   
            t.save() 
            return JsonResponse({"status": "done"}, status=200)

    # some error occured
        return JsonResponse({"error": "Status not upadated"}, status=400)
    except  Exception as e:
            return JsonResponse({"error": "Status not upadated "}, status=400)
 
       

def EditPassingYear(request):
    try:
        result = request.session['ADMIN']
        if is_ajax(request=request) and request.method == "POST":
            code = int(request.POST.get('code',None))
            aid = request.POST.get('activationid',None)
            

            PassingYear.objects.filter(id=aid).update(name=code)
            
            
            return JsonResponse({"status": "done"}, status=200)

    # some error occured
        return JsonResponse({"error": "Status not upadated"}, status=400)
    except  Exception as e:
            return JsonResponse({"error": "Status not upadated "}, status=400)
 
      
def DeletePassingYear(request):
    try:
        result = request.session['ADMIN']
        if is_ajax(request=request) and request.method == "POST":
            aid = request.POST.get('deleteaid',None)
            PassingYear.objects.filter(id=aid).delete()
            return JsonResponse({"status": "done"}, status=200)

    # some error occured
        return JsonResponse({"error": "Status not upadated"}, status=400)
    except  Exception as e:
            return JsonResponse({"error": "Status not upadated "}, status=400)
 
def getpaymentinfo(data):
    response={}
    total=120000
    paid=0
    try:
        for i in data:
            paid=paid+int(i.amount)  
        response['paid']=paid
        response['due']=total-paid
        return response
    except Exception as e:
       response['paid']=0
       response['due']=0
       return response 

def getapplication_status(applied):
    try:
        status=""
        if applied.status==1:
            status="Pending"
        elif applied.status==2:
            status="Rejected"
        elif applied.status==3 and applied.jobprofile.id!=17:
            status="Selected"
        elif applied.status==3 and applied.jobprofile.id==17 and applied.emp.regid == None:
            
            if applied.enroll_expire_date>timezone.now():
                status="Enrollment Pending"
            else:
                status="Enrollment Expired"    
        elif applied.status==3 and applied.jobprofile.id==17 and applied.emp.regid != None:
            status="Selected"    

        elif applied.status==4:
            status="Selected for interview"
        elif applied.status==5:
            status="Quit"
        elif applied.status==6:
            status="Hold for bda"
        elif applied.status==7:
            status="Interview is going on"
        return status
    except Exception as e:
        return None


def CandidateView(request,id):
    try:
        
        result = request.session['ADMIN']
        data=Applied.objects.filter(id=id)
        edu_data=EmpEducations.objects.filter(emp_id=data[0].emp.id)  
        try:
          statename=State.objects.using('CRTD-RC').get(state_id=data[0].emp.state_id).state_name
        except Exception as e:
            statename=None  
        try:
           distname=District.objects.using('CRTD-RC').get(dist_id=data[0].emp.dist_id).dist_name
        except Exception as e:
            distname=None 
        skill_data=EmpkeySkill.objects.filter(emp_id=data[0].emp.id)
        tip_payment_list=Tippayment.objects.filter(emp_id=data[0].emp.id).order_by("-payment_date")   ##for tip 
        tip_payment_info=getpaymentinfo(tip_payment_list)
        return render(request,'admin_temp/CandidateView.html', {
            'distname':distname,
        'statename':statename, 'id':id,'data':data,'edu_data':edu_data,'skill_data':skill_data,
        'tip_payment_list':tip_payment_list,"tip_payment_info":tip_payment_info,
        'applicationstatus':getapplication_status(data[0])
        
        })        
    
    except Exception as e:
        Logout(request) 
        return redirect('admin-login')


def StatusofCandidate(request): #selected for interview
    try:
        result = request.session['ADMIN']
        if is_ajax(request=request) and request.method == "POST":
            id = request.POST.get('_token',None)
            interview_date = request.POST.get('date',None)
            contact_name = request.POST.get('textname',None)
            contact_number = request.POST.get('textphone',None)
            address = request.POST.get('textadd',None)
            location = request.POST.get('location',None)
            instruction = request.POST.get('inst',None)

            status = request.POST.get('status_4',None)
            t=Applied.objects.filter(id=id)
            type_={1:"Internship",2:"Job" ,3:"CRTD Training Internship Program"}

            sendpushnotification(type_[t[0].type],"You Have Selected For Interview for "+t[0].jobprofile.name,t[0].emp.device_token,t[0].emp.id)
            
            t.update(status=status,interview_date=interview_date.split("T")[0]+" "+interview_date.split("T")[1],contactname=contact_name,contactno=contact_number,address=address,location=location,instruction=instruction,updated_at=timezone.now())
            return JsonResponse({"status": "done"}, status=200)

    # some error occured
        return JsonResponse({"error": "Status not upadated"}, status=400)
    except  Exception as e:
            return JsonResponse({"error": "Status not upadated "}, status=400)
def Generate_regid(applieddata):
    try:

        if applieddata.jobprofile.id==3 and applieddata.type==3:
            regid='CRTDTIP'+applieddata.emp.name[0:2].upper()
        elif applieddata.jobprofile.id==9 :
            regid='CRTDHR'+applieddata.emp.name[0:2].upper()

        if len(str(applieddata.emp.id))<2:
            regid=regid+"0"+str(applieddata.emp.id)
        else:
            regid=regid+str(applieddata.emp.id) 
        return regid    
    except Exception as e:
        pass                    

def UpdateCandidateStatus(request): #selected , Rejected
    try:
        result = request.session['ADMIN']
        if is_ajax(request=request) and request.method == "POST":
            applicationid = request.POST.get('applicationid',None)
            status = request.POST.get('status',None)
            
            applieddata=Applied.objects.get(id=applicationid)
            regid=None
            
            if applieddata.type==3 and status=="3":
                regid=Generate_regid(applieddata)
                emp=ApplyEmpInfo.objects.filter(id=applieddata.emp.id).update(regid=regid,selected_job_profile=applieddata.jobprofile)
            elif applieddata.type==1 and applieddata.apply_type==2 and status=="3" and applieddata.jobprofile.id==9 :
                regid=Generate_regid(applieddata)
                emp=ApplyEmpInfo.objects.filter(id=applieddata.emp.id).update(regid=regid,selected_job_profile=applieddata.jobprofile)
            
            mssg={
                "2":"You Have Rejected for ",
                "3":"You Have Selected for ",
                "5":"",
                "6":"",
                "7":"We would like to inform you that your application has been selected for the Interview. \n Your Interview is still in process. \n All the best for your results!",
            }
            type_={1:"Internship",2:"Job" ,3:"CRTD Training Internship Program"}
            sendpushnotification(type_[applieddata.type],mssg[status]+applieddata.jobprofile.name,applieddata.emp.device_token,applieddata.emp.id)
            Applied.objects.filter(id=applicationid).update(status=status,updated_at=timezone.now())
            if applieddata.jobprofile.id==17:
                 send_status_change_mail(int(status),applieddata.emp.email)
            return JsonResponse({"status": "done"}, status=200)
        return JsonResponse({"error": "Status not upadated"}, status=400)
    except  Exception as e:
            return JsonResponse({"error": "Status not upadated "}, status=400)

def Add_payment(request): #add tip payment from admin
    try:
        result = request.session['ADMIN']
        if is_ajax(request=request) and request.method == "POST":
            emp=ApplyEmpInfo.objects.get(id=request.POST.get('id',None))
            Tippayment.objects.create(emp=emp,amount=request.POST.get('amount',None),transactionid=request.POST.get('txnid',None),payment_date=request.POST.get('paymentdate',None),updated_at=timezone.now())
            
            return JsonResponse({"status": "done"}, status=200)
    # some error occured
        return JsonResponse({"error": "Status not upadated"}, status=400)
    except  Exception as e:
            return JsonResponse({"error": "Status not upadated "}, status=400)


def All_job_profile(request):
    try:
        result = request.session['ADMIN']
        jobprofiles=Job_profile.objects.all()
        return render(request,'admin_temp/alljobprofile.html',{'jobprofiles':jobprofiles})        
    except Exception as e:
        Logout(request)
        return redirect('admin-login')
def savedata(request):
    if is_ajax(request=request) and request.method == "POST":
        profile_name=request.POST["profile_name"]
        type=request.POST["type"]
        Sub_type=request.POST["Sub_Type"]
        Job_profile.objects.create(name=profile_name,type=type,sub_type=Sub_type,
        created_at=timezone.now(),status=1,hiretype=2)
        return redirect("admin-all_job_profile")

def save_feedback(request):
    try:
        result = request.session['ADMIN']
        if is_ajax(request=request) and request.method == "POST":
            feedback_taxt=request.POST["feedback_taxt"]
            appliedid=request.POST["appliedid"]            
            Applied.objects.filter(id=appliedid).update(feedback=feedback_taxt)
            return JsonResponse({"status": "done"}, status=200)
    # some error occured
        return JsonResponse({"error": "Status not upadated"}, status=400)
    except  Exception as e:
        return JsonResponse({"error": "Status not upadated "}, status=400)

def send_sms(request):
    import webbrowser as web
    temp={
            2:"Dear Candidate ,%0aThank you so much for your interest in the Business Development Associate position with our Company. We appreciate you taking the time to be a part of interview process with our team.%0a%0aWhile we were impressed with your skill set, we have chosen to proceed with another candidate who has more leadership experience.%0a%0aAgain, we appreciate your time, and we wish you the best of luck in your career endeavors.%0a%0aRegards,%0aCRTD Technologies Hiring Team",
            7:"""Dear Candidate,%0aHope you are doing fine!%0a
We would like to bring in your notice that your interview is still in process.%0a
All the best for your results!%0a%0a
Regards,%0a
CRTD Technologies Hiring Team""",
            3:"""
Dear Candidate,%0a
Congratulations, for getting selected in CRTD Technologies Pvt. Ltd.%0a
Now, you can moveahead for the further process. %0a
Simply, %0aClick on Enroll Now. %0a
Enter HR Code - CRTDHRRU10%0a
Voucher Code - Click No%0a
For any queries you can contact us on support@crtd.in %0a
Regards,%0a
CRTD Technologies Pvt. Ltd.
            """
        
        }

    try:
        result = request.session['ADMIN']
        if is_ajax(request=request) and request.method == "POST":

            id=request.POST["appliedid"]
            applieddata=Applied.objects.get(id=id)
            if applieddata.jobprofile.id==17:
                phone=applieddata.emp.phoneno
                phone="+91"+phone
                mssgtemp=temp[applieddata.status]
                web.open('https://web.whatsapp.com/send?phone='+phone+'&text='+mssgtemp)
            return JsonResponse({"status": "done"}, status=200)
    # some error occured
        return JsonResponse({"error": "not sent"}, status=400)
    except  Exception as e:
        return JsonResponse({"error": "not sent nn "}, status=400)



def update_whatsappstatus(request):
    try:
        result = request.session['ADMIN']
        if is_ajax(request=request) and request.method == "POST":

            id=request.POST["appliedid"]
            status=request.POST["status"]
            applieddata=Applied.objects.filter(id=id).update(whatsapp_status=status)
            return JsonResponse({"status": "done"}, status=200)
    # some error occured
        return JsonResponse({"error": "Status not upadated"}, status=400)
    except  Exception as e:
        return JsonResponse({"error": "Status not upadated "}, status=400)



        



