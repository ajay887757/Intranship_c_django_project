from django.shortcuts import redirect, render
from adminweb.isajax import get_month_max, is_ajax
from androidapi.models import Applied
from django.http import  JsonResponse
from datetime import *
from django.db.models import Q
from django.utils import timezone
from androidapi.sendmail import send_status_change_mail

from androidapi.sendnotification import sendpushnotification

def update_bda_status(request):
    try:
        result = request.session['ADMIN']
        if is_ajax(request=request) and request.method == "POST":
            id = request.POST.get('_token',None)
            enroll_expire_date = request.POST.get('date',None)
            amount_to_be_paid = request.POST.get('textamount',None)
            t=Applied.objects.filter(id=id)
            type_={1:"Internship",2:"Job" ,3:"CRTD Training Internship Program"}

            sendpushnotification(type_[t[0].type],"You Have Selected For  "+t[0].jobprofile.name+" open app and enroll now",t[0].emp.device_token,t[0].emp.id)
            t.update(status=3,enroll_expire_date=enroll_expire_date,amount_to_paid=amount_to_be_paid,updated_at=datetime.now())
                       
            send_status_change_mail(3,t[0].emp.email)
            return JsonResponse({"status": "done"}, status=200)
        return JsonResponse({"error": "Status not upadated"}, status=400)
    except  Exception as e:
        
            return JsonResponse({"error": "Status not upadated "}, status=400)


def get_bda_data(timemin,timemax,today_min,today_max,type,jobcode_type):
    try:
        Alldata=Applied.objects.filter(jobprofile__id=17,jobcode__code_type=jobcode_type,updated_at__range=(timemin,timemax))
        if type=='all':
            totalapplied=Alldata.filter(status=1).count()
            totalselected=Alldata.filter(status=3).exclude(amount_paid=None).count()
            totalrejected=Alldata.filter(status=2).count()
            total_enrollment_expired=Alldata.filter(status=3,emp__regid=None,enroll_expire_date__lt=timezone.now()).count()
            enrollmentpending=Alldata.filter(Q(status=3),Q(emp__regid=None),Q(enroll_expire_date__gt=timezone.now())).count()
            enrollmenthold=Alldata.filter(Q(status=6)).count()
            selected_for_enrollment=Alldata.filter(Q(status=3),Q(enroll_expire_date__gt=timezone.now()),Q(emp__regid=None)).count()
            interview_going_on_bda=Alldata.filter(status=7).count()
            return totalapplied,totalselected,totalrejected,total_enrollment_expired,enrollmentpending,enrollmenthold,selected_for_enrollment,interview_going_on_bda
        elif type=='applied':
            return Alldata.filter(status=1)
        elif type=="Rejected":
            return Alldata.filter(status=2)
        elif type=="Enrollment Pending":
            return Alldata.filter(Q(status=3),Q(emp__regid=None),Q(enroll_expire_date__gt=timezone.now()))
        elif type=="Enrollment Hold":
            return Alldata.filter(Q(status=6))
        elif type=="Selected":
            return Alldata.filter(status=3).exclude(amount_paid=None)
        elif type=="Expired enrollments":
            return Alldata.filter(status=3,enroll_expire_date__lt=datetime.today(),emp__regid=None)
        elif type=="selected_for_enrollment":
            return Alldata.filter(Q(status=3),Q(enroll_expire_date__gt=datetime.today()),Q(emp__regid=None))
        elif type=="interview_going_on_bda":
            return Alldata.filter(status=7)
        
    except Exception as e:
        pass

def bda_candidate_list(request,month,year,type,hiring_type):
    try:
        today_min = datetime.combine(date.today(), time.min)
        today_max = datetime.combine(date.today(), time.max)
        month_min=(datetime.now().replace(day=1).replace(month=int(month)).replace(year=int(year)))
        month_max=get_month_max(year,month)
        data=get_bda_data(month_min,month_max,today_min,today_max,type,hiring_type)
        return render(request,'admin_temp/candidatelist.html',{'res':data,"title":type+" Bda"})    

    except Exception as e:
        pass

def update_bda_enrollment_details(request):
    try:
        result = request.session['ADMIN']
        if is_ajax(request=request) and request.method == "POST":
            empid = request.POST.get('_token',None)
            enroll_expire_date = request.POST.get('enrollment_date',None)
            amount_to_be_paid = request.POST.get('enrollment_amount',None)
            t=Applied.objects.filter(id=empid)
            type_={1:"Internship",2:"Job" ,3:"CRTD Training Internship Program"}

            sendpushnotification(type_[t[0].type],"Your got a new Enrollment details, open app",t[0].emp.device_token,t[0].emp.id)

            t.update(status=3,enroll_expire_date=enroll_expire_date,amount_to_paid=amount_to_be_paid,updated_at=datetime.now())
            return JsonResponse({"status": "done"}, status=200)
    # some error occured
        return JsonResponse({"error": "Status not upadated"}, status=400)
    except  Exception as e:
            return JsonResponse({"error": "Status not upadated "}, status=400)

