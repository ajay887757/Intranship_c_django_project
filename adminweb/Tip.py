from django.shortcuts import render
from django.shortcuts import redirect
from datetime import *

from adminweb.views import Logout, get_month_max, getAppliedCount

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
    return month_min,month_max,month,year

def ShowtipState(request,id):
    try:
        name={1:"Pending",2:"Rejected",3:"Selected" ,4:"Selected For Interview"}
        result = request.session['ADMIN']
        today_min = datetime.combine(date.today(), time.min)
        today_max = datetime.combine(date.today(), time.max)
        month_min,month_max,month,year=gettime(request)
        result = request.session['ADMIN']
        today=getAppliedCount(3,1,id,None,today_min,today_max).count()
        total=getAppliedCount(3,1,id,None,month_min,month_max).count()
        todaydate=date.today().strftime('%Y/%m/%d')
        param={
            "today":today,
            "total":total,
            "month":month,
            "year":year,
            'title':name[id],
            'todaydate':todaydate,
            "status":id 

            
        }
        return render(request,"admin_temp/Tipstate.html",param)
    except Exception as e:
          print(e)
          Logout(request)
          return redirect('admin-login')

def Tip_candidate_list(request,total_today,status,year,month):
    try:
        name={1:"Pending",2:"Rejected",3:"Selected" ,4:"Selected For Interview"}
        result = request.session['ADMIN']
        today_min = datetime.combine(date.today(), time.min)
        today_max = datetime.combine(date.today(), time.max)
        month_min =(datetime.now().replace(day=1).replace(month=int(month)).replace(year=int(year)) )
        month_max=get_month_max(year,month)
        result = request.session['ADMIN']

        if(total_today=='total'):
            data=getAppliedCount(3,1,status,None,month_min,month_max)
        else:
           data=getAppliedCount(3,1,status,None,today_min,today_max)
        param={
            'title':name[status],
            'res':data,
        }
        return render(request,'admin_temp/candidatelist.html',param)  
    except Exception as e:
          print(e)
        #   Logout(request)
          return redirect('admin-login')  