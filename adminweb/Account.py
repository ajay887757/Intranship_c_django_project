from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect
from datetime import *

from adminweb.views import Logout, get_month_max, is_ajax
from androidapi.models import ApplyEmpInfo

def gettime(request):

    if(request.POST.get('cmonth')!=None):
        month=int(request.POST.get('cmonth'))
    elif(request.POST.get('cmonth')==None):
        month=datetime.now().month
  
    if(request.POST.get('cyear')!=None):
        year=int(request.POST.get('cyear'))
        
    elif(request.POST.get('cyear')==None):
        year=datetime.now().year
        


    month_min=(datetime.now().replace(day=1).replace(month=int(month)).replace(year=int(year)) )
    month_max=get_month_max(year,month)
    return month_min,month_max,year,month

def getShowaccountdata(time_min,time_max,verification_status):
    try:
        data=ApplyEmpInfo.objects.filter(created_at__range=(time_min, time_max),profile_status=verification_status).order_by('updated_at')
        return data
    except Exception as e:
        return []

def ShowAccountstate(request,type):
    try:
        result = request.session['ADMIN']
        today_min = datetime.combine(date.today(), time.min)
        today_max = datetime.combine(date.today(), time.max)
        month_min,month_max,year,month=gettime(request)
        verified=None
        unverified=None
        if type=='today':
         verified=getShowaccountdata(today_min,today_max,1).count() #today account created
         unverified=getShowaccountdata(today_min,today_max,0).count() #today account created
         Registered=ApplyEmpInfo.objects.filter(created_at__range=(today_min, today_max)).count()
        else: #total
         verified=getShowaccountdata(month_min,month_max,1).count() #today account created
         unverified=getShowaccountdata(month_min,month_max,0).count() #today account created
         Registered=ApplyEmpInfo.objects.filter(created_at__range=(month_min, month_max)).count()


       
        param={
            "type":type,
            "verified":verified,
            "unverified":unverified,
            "Registered":Registered,
            'year':year,
            'month':month,

            } 
        return render(request,"admin_temp/Account/account.html",param)
    except Exception as e:
          Logout(request)
          return render(request, "admin_temp/Login.html", {'msg': 'Server Error'})

def Showaccounts_list(request,total_today,account_status,year,month):
    try:
        result = request.session['ADMIN']
        today_min = datetime.combine(date.today(), time.min)
        today_max = datetime.combine(date.today(), time.max)
        month_min =(datetime.now().replace(day=1).replace(month=int(month)).replace(year=int(year)) )
        month_max=get_month_max(year,month)
        accounts=[]
        if total_today=='total' :
            if  account_status==2: #only registered
                accounts=ApplyEmpInfo.objects.filter(created_at__range=(month_min, month_max)).order_by("updated_at")
            else:
                accounts=getShowaccountdata(month_min,month_max,account_status) 

        elif total_today=='today' :
            if  account_status==2: #only registered
                accounts=ApplyEmpInfo.objects.filter(created_at__range=(today_min, today_max)).order_by("updated_at")
            else:
                accounts=getShowaccountdata(today_min,today_max,account_status) #today account created
        
        return render(request,"admin_temp/Account/Allaccountslist.html",{'accounts':accounts})
    except Exception as e:
        Logout(request)
        return render(request, "admin_temp/Login.html", {'msg': 'Server Error'})

def change_account_status(request):
    try:
        result = request.session['ADMIN']
        if is_ajax(request=request) and request.method == "POST":
            status = request.POST.get('status',None)
            empid = request.POST.get('empid',None)
            ApplyEmpInfo.objects.filter(id=empid).update(status=status)
            return JsonResponse({"status": "done"}, status=200)
    # some error occured
        return JsonResponse({"error": "Status not upadated"}, status=400)
    except Exception as e:
        # Logout(request)
        return JsonResponse({"error": "Status not upadated "}, status=400)

#only for hr
def change_canhire_status(request):
    try:
        result = request.session['ADMIN']
        if is_ajax(request=request) and request.method == "POST":
            status = request.POST.get('status',None)
            empid = request.POST.get('empid',None)
            ApplyEmpInfo.objects.filter(id=empid).update(canhirestatus=status)
            return JsonResponse({"status": "done"}, status=200)
    # some error occured
        return JsonResponse({"error": "Status not upadated"}, status=400)
    except Exception as e:
        # Logout(request)
        return JsonResponse({"error": "Status not upadated "}, status=400)
      