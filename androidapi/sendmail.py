import json
from django.http import HttpResponse, HttpResponseRedirect
import requests
from django.conf import settings
from django.core.mail import send_mail

def send_acc_creation_mail(name,email,password):
    try:
        param=dict()
        param['name']=name
        param['mail']=email
        param['pass']=password
        post_data = json.dumps(param)

        requests.post("http://crtd.in/acc_creation_mail.php", data = post_data, headers = {"Content-type": "application/json"}).json()
    except Exception as e:
        pass

def send_enrollment_mail(regid,mail,name):
    try:
        param=dict()
        param['name']=name
        param['mail']=mail
        param['id']=regid
        post_data = json.dumps(param)

        requests.post("http://researchcenter.crtd.in/android/phpdb/surveyur_manager/testmail.php", data = post_data, headers = {"Content-type": "application/json"}).json()
    except Exception as e:
        pass

def send_status_change_mail(status,mail):
    try:
        temp={
            2:"""
Dear Candidate ,

Thank you so much for your interest in the Business Development Associate position with our Company. We appreciate you taking the time to be a part of interview process with our team.
 

While we were impressed with your skill set, we have chosen to proceed with another candidate who has more leadership experience.
 

Again, we appreciate your time, and we wish you the best of luck in your career endeavors.
 

Regards,

CRTD Technologies Hiring Team
              """,
            7:"""Dear Candidate,

Hope you are doing fine!

We would like to bring in your notice that your interview is still in process.

All the best for your results!


Regards,
CRTD Technologies Hiring Team""",
3:"""
Dear Candidate,

Congratulations, for getting selected in CRTD Technologies Pvt. Ltd.

Now, you can moveahead for the further process. 

Simply, Click on Enroll Now. 

Enter HR Code - CRTDHRRU10

Voucher Code - Click No

For any queries you can contact us on support@crtd.in 

Regards, 
CRTD Technologies Pvt. Ltd.
            """

       
        }

        mssgtemp=temp[status]

        
        
        param=dict()
        param['mssg']=mssgtemp
        param['mail']=mail
        post_data = json.dumps(param)

        requests.post("http://crtd.in/status_change_mail.php", data = post_data, headers = {"Content-type": "application/json"})
    except Exception as e:
        pass

def send_mail_e(request):
    try:
        subject = 'welcome to GFG world'
        message = f'Hi shivam, thank you for registering in geeksforgeeks.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['shivamthakurcool01@gmail.com', ]
        send_mail( subject, message, email_from, recipient_list )
        return HttpResponse("hii")
    except Exception as e:
        print(e)
        return HttpResponse(e)
