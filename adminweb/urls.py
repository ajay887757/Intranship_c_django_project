"""wyreflowtask URL Configuration

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
from os import name
from django.contrib import admin
from django.urls import path
from scipy.__config__ import show
from adminweb import views
from adminweb.Account import ShowAccountstate, Showaccounts_list, change_account_status
from adminweb.Bda import *
from adminweb.Tip import ShowtipState, Tip_candidate_list
from androidapi.sendmail import  send_mail_e
from adminweb.Vouchercode import Editvouchercode, addvouchercode, get_all_vouchercode
urlpatterns = [
    # path('adminweb/', adminweb.site.urls),

    path('admin-login/',views.Login,name='admin-login'),
    path('admin-checklogin',views.CheckAdminLogin),
    path('admin-dashboard/',views.Admindashboard,name='admin-dashboard'),
    path('internship_view/<int:id>',views.InternshipView,name='internship_view'),
    path('candidatelist/<int:id>/<str:id1>/<int:id2>/<int:id3>/<str:title>',views.candidatelist,name='candidatelist'),
    path('admin-candidateview',views.CandidateView,name='admin-candidateview'),
    path('admin-drawer/<int:id>',views.Drawer,name='admin-drawer'),
    
    path('admin-addactivationcode',views.Addactivationcode,name='admin-addactivationcode'),
    path('admin-editactivationcode',views.Editactivationcode,name='admin-editactivationcode'),
    path('admin-deleteactivationcode',views.Deleteactivationcode,name='admin-deleteactivationcode'),
    path('admin-addpassingyear',views.AddPassingYear,name='admin-addpassingyear'),
    path('admin-editpassingyear',views.EditPassingYear,name='admin-editpassingyear'),
    path('admin-deletepassingyear',views.DeletePassingYear,name='admin-deletepassingyear'),
    path('admin-all_job_profile',views.All_job_profile,name='admin-all_job_profile'),

#college
 path('admin-addcollege',views.Addcollege,name='admin-addcollege'),
    path('admin-editclgname',views.Editclgname,name='admin-editclgname'),
    path('admin-deleteclg',views.Deleteclg,name='admin-deleteclg'),
    path('admin-clgstatus',views.update_clgstatus,name='admin-clgstatus'),

#canidate view
  path('admin-candidateview/<int:id>',views.CandidateView,name='admin-candidateview'),

 path('admin-statusofcandidate',views.StatusofCandidate,name='admin-statusofcandidate'),
 path('admin-updatestatus',views.UpdateCandidateStatus,name='admin-updatestatus'),

#tip
    path('admin-tipstatus/<int:id>',ShowtipState,name='admin-tipstatus'),
    path('admin-addtippayment',views.Add_payment,name='admin-addtippayment'),
    path('admin-tip_applicationlist/<str:total_today>/<int:status>/<int:year>/<int:month>/',Tip_candidate_list,name='admin-tip_applicationlist'),

#account
    path('admin-accountstates/<str:type>',ShowAccountstate,name='admin-accountstates'),
    path('admin-accountslist/<str:total_today>/<int:account_status>/<int:year>/<int:month>/',Showaccounts_list,name='admin-accountslist'),

#emp status
    path('admin-changeacntstatus',change_account_status,name='admin-changeacntstatus'),
    path('admin-changecanhirestatus',change_account_status,name='admin-changecanhirestatus'),

#bda
    path('admin-select_bda/',update_bda_status,name='admin-select_bda'),
    path('admin-update_enrollment_details/',update_bda_enrollment_details,name='admin-update_enrollment_details'),

#jobcode
    path('admin-addjobcode',views.Addjobcode,name='admin-addjobcode'),
    path('admin-editjobcode',views.Editjobcode,name='admin-editjobcode'),
    path('save_job/',views.savedata,name="savedata"),
    path('admin-bda_candidate_list/<int:month>/<int:year>/<str:type>/<int:hiring_type>/',bda_candidate_list,name="bda_candidate_list"),
    
#voucher
#     
    path('admin-voucher/',get_all_vouchercode,name="admin-voucher"),
    path('admin-addvouchercode/',addvouchercode,name="admin-addvouchercode"),
    path('admin-editvouchercode/',Editvouchercode,name="admin-editvouchercode"),
    path('admin-save_feedback/',views.save_feedback,name="admin-save_feedback"),
    path("admin-whatsapp_message/",views.send_sms,name="admin-whatsapp_message"),
    
    path("admin-update_whatsappstatus/",views.update_whatsappstatus,name="admin-update_whatsappstatus"),




]
