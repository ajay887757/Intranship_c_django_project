"""crtdapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.urls import path
from androidapi.FORGOTPASSWORD.Changepass import Change_password
from androidapi.FORGOTPASSWORD.otp import Send_mail_otp
from androidapi.trans import create

from androidapi.version import Get_appversion

from .views import CHANGE_LOGINPIN, CHECK_HR_CODE_VOUCHER, GET_ALL_STATE, GET_BDA_CAMPUS_TYPE, GET_DISTRICT, GET_STREAM, SAVE_BDA_PAYMENT, SAVE_DEVICE_TOKEN, Add_Fullsizephoto, Add_contactus, Add_hq, Add_skill, Applied_login, Apply_, Apply_emp_edu, Apply_empinfo, Change_workingStatus, Check_Applied, Check_crna_data, Create_account, GET_HIRING_work_status, Get_Keyskills, Get_applied, Get_board, Get_clg, Jobprofile, Save_Aadhar, Tip_tranx_token, TipApply_, TipCheckCode, Tippaymentinfo, Tipsaverepayment, Update_Address, Update_hq, check_jobcode,Get_passingyear

# from upload

urlpatterns = [
    path('android/crtdtech-emp-checkjobcode', check_jobcode.as_view()),
    path('android/crtdtech-get-college', Get_clg.as_view()),
    path('android/crtdtech-get-py', Get_passingyear.as_view()), #get passging year
    path('android/crtdtech-get-board', Get_board.as_view()), #get passging year
    path('android/crtdtech-get-empkeyskill', Get_Keyskills.as_view()), #get passging year
    path('android/crtdtech-save-aadhar', Save_Aadhar.as_view()), #get passging year
    path('android/crtdtech-check-crna-data', Check_crna_data.as_view()), #get passging year
    path('android/crtdtech-crna-data', Create_account.as_view()), #get passging year
    path('android/crtdtech-add-hq', Add_hq.as_view()), #get passging year
    path('android/crtdtech-update-hq', Update_hq.as_view()), #get passging year
    path('android/crtdtech-update-add', Update_Address.as_view()), #get passging year
    path('android/crtdtech-update-keyskills', Add_skill.as_view()), #get passging year
    path('android/crtdtech-update-fullsizeimg', Add_Fullsizephoto.as_view()), #get passging year
    path('android/crtdtech-login', Applied_login.as_view()), #get passging year
    path('android/crtdtech-empinfo', Apply_empinfo.as_view()), #get passging year
    path('android/crtdtech-empedu', Apply_emp_edu.as_view()), #get passging year
    
    #applied url
    path('android/crtdtech-checkapplied', Check_Applied.as_view()), #get passging year
    path('android/crtdtech-apply', Apply_.as_view()), #get passging year
    path('android/crtdtech-jp', Jobprofile.as_view()), #get passging year
    path('android/crtdtech-getapplied', Get_applied.as_view()), #get passging year

#version
    path('android/crtdtech-main-version', Get_appversion.as_view()), #get passging year
 
 #forgot password
     path('android/crtdtech-sendotp', Send_mail_otp.as_view()), #get passging year
     path('android/crtdtech-matchotp', Send_mail_otp.as_view()), #get passging year
     path('android/crtdtech-changepassword', Change_password.as_view()), #get passging year

#contact us
     path('android/crtdtech-contactus', Add_contactus.as_view()), #get passging year

#tip 
     path('android/crtdtech-tip-checkcode', TipCheckCode.as_view()), #get passging year
     path('android/crtdtech-tip-txntoken', Tip_tranx_token.as_view()), #get passging year
     path('android/crtdtech-tip-apply', TipApply_.as_view()), #get passging year
     path('android/crtdtech-tip-getpayment', Tippaymentinfo.as_view()), #get passging year
     path('android/crtdtech-tip-repayment', Tipsaverepayment.as_view()), #get passging year
#hr
     path('android/crtdtech-hr-hiringstatus', GET_HIRING_work_status.as_view()), #get passging year

#emp
     path('android/crtdtech-emp-changeworkstatus', Change_workingStatus.as_view()), #get passging year
     path('android/crtdtech-emp-getstates', GET_ALL_STATE.as_view()), #get passging year
     path('android/crtdtech-emp-getdistrict', GET_DISTRICT.as_view()), #get passging year
     path('android/crtdtech-emp-check_hr_code_voucher', CHECK_HR_CODE_VOUCHER.as_view()), #get passging year
     path('android/crtdtech-emp-save_device_token', SAVE_DEVICE_TOKEN.as_view()), #get passging year
     path('android/crtdtech-emp-getstream', GET_STREAM.as_view()), #get passging year
     path('android/crtdtech-emp-changepin', CHANGE_LOGINPIN.as_view()), #get passging year

#bda
     path('android/crtdtech-bda-savepayment', SAVE_BDA_PAYMENT.as_view()), #get passging year
     path('android/crtdtech-bda-campustype', GET_BDA_CAMPUS_TYPE.as_view()), #get passging year
     path('trans', create), #get passging year


]
