# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models
from django.utils import timezone
from django.utils.timezone import now


class Adminlogins(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255, blank=True, null=True)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=500, blank=True, null=True)
    registration_id = models.CharField(max_length=500, blank=True, null=True)
    user_image = models.CharField(max_length=500, blank=True, null=True)
    user_status = models.CharField(max_length=5)
    password = models.CharField(max_length=255)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True,auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'adminlogins'

class JobCode(models.Model):
    id = models.BigIntegerField(primary_key=True)
    code = models.CharField(max_length=20)
    valid_date = models.DateTimeField(blank=True, null=True)
    code_type=models.IntegerField(default=1)  #1 offCampus 2:On Campus
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'JobCode'

class TIPActivationCode(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=20)
    valid_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'tipactivation_code'


class Appversion(models.Model):
    version = models.CharField(max_length=20)
    link = models.TextField()
    type = models.IntegerField()
    changes = models.TextField()
    created_at = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'appversion'




class College(models.Model):
    name = models.CharField(max_length=250)
    status = models.IntegerField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'college'




class ApplyEmpInfo(models.Model):
    name = models.CharField(max_length=50)
    phoneno = models.CharField(max_length=11)
    fullsizephoto=models.CharField(max_length=250,default=None)
    whphoneno = models.CharField(max_length=11)
    email = models.CharField(max_length=200)
    password = models.TextField()
    profile_status=models.IntegerField() #1:verified 0:not verified 
    course_type = models.ForeignKey("Stream_type",on_delete=models.DO_NOTHING)
    Aadhar_front_img = models.CharField(max_length=200,null=True,blank=True)
    Aadhar_back_img = models.CharField(max_length=200,null=True,blank=True)
    paddress = models.TextField( blank=True, null=True) #permanent address
    caddress = models.TextField( blank=True, null=True) #Current Address
    college = models.ForeignKey("College",db_column='college',on_delete=models.CASCADE)
    passing_year = models.ForeignKey("PassingYear",db_column='passing_year',on_delete=models.CASCADE)
    branch = models.IntegerField(blank=True, null=True)
    photo = models.CharField(max_length=250)
    resume = models.CharField(max_length=250,null=True)
    longitude = models.CharField(max_length=100)
    lattitude = models.CharField(max_length=100)
    gender= models.IntegerField() #1:male 2:female
    status=models.IntegerField(default=1,null=True) #1:active 2:inactive
    canhirestatus=models.IntegerField(default=0,null=True) #1:yes 2:no
    regid=models.CharField(max_length=40,default=None,null=True)
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_created=True,default=None,blank=True)
    state_id=models.IntegerField(default=None,null=True)
    dist_id=models.IntegerField(default=None,null=True)
    loginpin=models.CharField(max_length=5,default=None,null=True)
    referal_code=models.CharField(max_length=50,default=None,null=True)
    selected_job_profile=models.ForeignKey("Job_profile",on_delete=models.DO_NOTHING,null=True,default=None)
    dob=models.DateField(default=None,null=True)
    device_token=models.CharField(max_length=250,null=True,default=None)
    class Meta:
        managed = True
        db_table = 'apply_emp_info'


class PassingYear(models.Model):
    name = models.IntegerField()
    created_at = models.DateTimeField(auto_created=True)

    class Meta:
        db_table = 'passing_year'
class Board(models.Model):
    name=models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_created=True)

    class Meta:
        db_table='board'


class EmpkeySkill(models.Model):
    created_at = models.DateTimeField()
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=50)
    emp = models.ForeignKey(ApplyEmpInfo, models.DO_NOTHING)
    class Meta:
        managed = True
        db_table = 'empkeyskill'  
     
class EmpEducations(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.BigAutoField(primary_key=True)
    hq_type = models.IntegerField()  #1:class XII 2:class X
    school_medium = models.IntegerField(blank=True, null=True)
    total_marks = models.CharField(max_length=5, blank=True, null=True)
    board = models.ForeignKey(Board, models.DO_NOTHING, blank=True, null=True)     
    emp = models.ForeignKey(ApplyEmpInfo, models.DO_NOTHING,default=None)
    py = models.ForeignKey('PassingYear', models.DO_NOTHING,default=None)

    class Meta:
        managed = True
        db_table = 'emp_educations'

class Job_profile(models.Model):
    name=models.CharField(max_length=100)
    status=models.IntegerField()
    type=models.IntegerField() #1:internship 2:job 3:tip
    sub_type=models.IntegerField()  #1:tech  2:hr 3:other
    hiretype=models.IntegerField() #1 offCampus 2:On Campus
    created_at = models.DateTimeField(auto_created=True)

    class Meta:
        db_table='job_profile'

class Applied(models.Model):

    emp=models.ForeignKey(ApplyEmpInfo,models.DO_NOTHING,default=None)
    apply_type=models.IntegerField() #1:technical internship 2:HR internship
    type=models.IntegerField() #1:Internship 2:Job 3:TIP
    jobprofile=models.ForeignKey(Job_profile,models.DO_NOTHING,default=None) #1:full stack developer 2:front-end 3:backend 4:android
    status=models.IntegerField(null=True) #1:pending 2: rejected 3:selected 4:Selected for interview 5:quit 6:hold for bda 7:Interview is going on
    interview_date=models.DateTimeField(null=True)
    contactname=models.CharField(max_length=100,default=None,null=True)
    contactno=models.CharField(max_length=10,default=None,null=True)
    location=models.CharField(max_length=50,default=None,null=True) #it contain lattitude and longitude
    address=models.TextField(default=None,null=True) #it contain lattitude and longitude
    instruction=models.TextField(default=None,null=True) #it contain lattitude and longitude
    Transactionid=models.CharField(max_length=100,default=None,null=True)
    amount_to_paid=models.CharField(max_length=50,default=None,null=True)
    amount_paid=models.CharField(max_length=50,default=None,null=True)
    voucher_code=models.CharField(max_length=100,default=None,null=True)
    enroll_expire_date=models.DateTimeField(default=None,null=True)
    payment_date=models.DateTimeField(default=None,null=True)
    jobcode=models.ForeignKey(JobCode,on_delete=models.DO_NOTHING,default=None,null=True)
    feedback=models.TextField(default=None,null=True)
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)
    whatsapp_status=models.IntegerField(default=0,null=True)

    class Meta:
        managed = True
        db_table = 'applied'

class Contactus(models.Model):
    name=models.CharField(max_length=100) 
    email=models.CharField(max_length=250)
    phoneno=models.CharField(max_length=10)
    message=models.TextField()
    created_at=models.DateTimeField(default=timezone.now)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        db_table='contactus'
class Tippayment(models.Model):
    emp=models.ForeignKey(ApplyEmpInfo,on_delete=models.CASCADE,default=None)
    amount=models.CharField(max_length=10)
    transactionid=models.CharField(max_length=100,default=None,null=True)
    payment_date=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        managed=True
        db_table='tippayment'            
class TipCampusexecutive(models.Model):
    emp=models.OneToOneField(ApplyEmpInfo,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        db_table='TipCampusexecutive'
class HrTarget(models.Model):
    emp=models.ForeignKey(ApplyEmpInfo,on_delete=models.CASCADE)
    target=models.CharField(max_length=5)
    month=models.IntegerField()
    created_at=models.DateTimeField(auto_created=True,default=now)                            
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        db_table='hrtarget'
class EmpReport(models.Model):
    emp=models.ForeignKey(ApplyEmpInfo,on_delete=models.CASCADE)
    workingstatus=models.IntegerField()
    created_at=models.DateTimeField(auto_created=True,default=now)                            
    updated_at=models.DateTimeField(auto_now=True)   
    class Meta:
        db_table='empreport'
class Voucher_Code(models.Model):
    code = models.TextField()
    price = models.TextField()
    status = models.IntegerField()
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_created=True)

    class Meta:
        managed = True
        db_table = 'voucher_code'  


class Stream_type(models.Model):
    name = models.TextField()
    status = models.IntegerField()
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_created=True)

    class Meta:
        managed = True
        db_table = 'stream_type'
