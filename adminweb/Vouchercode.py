from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import redirect, render
from adminweb.isajax import is_ajax
from adminweb.views import Logout
from androidapi.models import Voucher_Code

def get_all_vouchercode(request):
    try:
        result = request.session['ADMIN']
        Vouchers=Voucher_Code.objects.all()
        return render(request,'admin_temp/Vouchercode.html',{'Vouchers':Vouchers,})    
    except Exception as e:
        Logout(request)
        return redirect('admin-login')

def addvouchercode(request):
    try:
        result = request.session['ADMIN']
        if is_ajax(request=request) and request.method == "POST":
            code = request.POST.get('addcode',None)
            price = request.POST.get('addprice',None)
            r=Voucher_Code.objects.all().values("code")
            for i in r:
                if(i['code']==code):
                    return JsonResponse({"error": "Already exists"}, status=400)
            t=Voucher_Code.objects.create(code=code,price=price,status=1, created_at=datetime.now(),updated_at=datetime.now())               
            return JsonResponse({"status": "done"}, status=200)

    # some error occured
        return JsonResponse({"error": "Status not upadated"}, status=400)
    except  Exception as e:
            return JsonResponse({"error": "Status not upadated "}, status=400)
 
def Editvouchercode(request):
    try:
        result = request.session['ADMIN']
        if is_ajax(request=request) and request.method == "POST":

            code = request.POST.get('code',None)
            vid = request.POST.get('activationid',None)
            price = request.POST.get('price',None)
            
            Voucher_Code.objects.filter(id=vid).update(code=code,price=price)
           
            
            return JsonResponse({"status": "done"}, status=200)

    # some error occured
        return JsonResponse({"error": "Status not upadated"}, status=400)
    except  Exception as e:
            print(e)
            return JsonResponse({"error": "Status not upadated "}, status=400)
 
           