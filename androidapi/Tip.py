import requests
import json
from paytmchecksum import PaytmChecksum
from androidapi.models import TIPActivationCode,Applied,Job_profile,ApplyEmpInfo, Tippayment
from datetime import date, datetime


def Tipcheckcode(code1):
    try:
        code=TIPActivationCode.objects.filter(code=code1).values()
        return code
    except :
        pass






def gettxttoken(orderid,costumerid,price):
    paytmParams = dict()
    try:
        paytmParams["body"] = {
        "requestType":"Payment",
        "mid": "cZvXNb71330776380242",
        "websiteName": "crtd",
        "orderId": orderid,
        "callbackUrl": "https://securegw.paytm.in/theia/paytmCallback?ORDER_ID="+orderid,
        "txnAmount": {
        "value": str(price),
        "currency": "INR",
        },
        "userInfo": {
            "custId":costumerid,
        },
        "enablePaymentMode":[{"mode" : "UPI"}],
            "disablePaymentMode": [{"mode" : "PPBL"}]
      
        }
            
        # Generate checksum by parameters we have in body
        # Find your Merchant Key in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys 
        checksum = PaytmChecksum.generateSignature(json.dumps(paytmParams["body"]), "lEQDqnYLX8uASo%1")

        paytmParams["head"] = {
                "signature": checksum
            }
        post_data = json.dumps(paytmParams)
        

        # for Staging
        url = "https://securegw.paytm.in/theia/api/v1/initiateTransaction?mid=cZvXNb71330776380242&orderId="+orderid
        response = requests.post(url, data = post_data, headers = {"Content-type": "application/json"}).json()
        response1={}
      
        response1["token"]=response['body']['txnToken']
        
        return response1
    except Exception as e:
        pass

#save tip registration amount
def Tipappply(empid,apply_type,jobprofiletype,type,txnid):
    response={}
    try:
        
            emp=ApplyEmpInfo.objects.get(id=empid)
            jp=Job_profile.objects.get(id=jobprofiletype)
            Applied.objects.create(Transactionid=txnid,emp=emp,apply_type=apply_type,type=type, status=1,jobprofile=jp, created_at=datetime.now(),updated_at=datetime.now())
            response['mess']='100' #done
            return response
    except Exception as e:
        response['mess']='500'
        return response


def Getpaymentinfo(empid):
    response={}
    total=120000
    paid=0
    try:
        tippayment=Tippayment.objects.filter(emp__id=empid)
        for i in tippayment:
            paid=paid+int(i.amount)  
        response['paid']=paid
        response['due']=total-paid
        return response
    except Exception as e:
       response['paid']=0
       response['due']=0
       return response

def Tipsave_payment(empid,amount,txnid): #save 1,20,000  tip payment 
    response={}
    try:
            emp=ApplyEmpInfo.objects.get(id=empid)
            Tippayment.objects.create(emp=emp,amount=amount,transactionid=txnid,payment_date=datetime.now(),updated_at=datetime.now())
            response['mess']='100' #done
            return response
    except Exception as e:
        response['mess']='500'
        return response


