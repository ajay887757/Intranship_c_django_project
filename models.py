# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ActivationCode(models.Model):
    code = models.CharField(max_length=20)
    valid_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'activation_code'


class Applied(models.Model):
    created_at = models.DateTimeField()
    id = models.BigAutoField(primary_key=True)
    apply_type = models.IntegerField()
    status = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField()
    emp = models.ForeignKey('ApplyEmpInfo', models.DO_NOTHING)
    jobprofile = models.ForeignKey('JobProfile', models.DO_NOTHING)
    type = models.IntegerField()
    interview_date = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    contactname = models.CharField(max_length=100, blank=True, null=True)
    contactno = models.CharField(max_length=10, blank=True, null=True)
    instruction = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'applied'


class ApplyEmpInfo(models.Model):
    name = models.CharField(max_length=50)
    phoneno = models.CharField(max_length=11)
    whphoneno = models.CharField(max_length=11)
    email = models.CharField(max_length=200)
    password = models.TextField()
    course_type = models.IntegerField()
    college = models.IntegerField()
    passing_year = models.IntegerField()
    branch = models.IntegerField(blank=True, null=True)
    photo = models.CharField(max_length=250)
    resume = models.CharField(max_length=250)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    caddress = models.TextField(blank=True, null=True)
    paddress = models.TextField(blank=True, null=True)
    aadhar_back_img = models.CharField(db_column='Aadhar_back_img', max_length=200, blank=True, null=True)  # Field name made lowercase.
    aadhar_front_img = models.CharField(db_column='Aadhar_front_img', max_length=200, blank=True, null=True)  # Field name made lowercase.
    profile_status = models.IntegerField()
    gender = models.IntegerField()
    lattitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'apply_emp_info'


class Appversion(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.CharField(max_length=20)
    link = models.TextField()
    type = models.IntegerField()
    changes = models.TextField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'appversion'


class Board(models.Model):
    created_at = models.DateTimeField()
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'board'


class College(models.Model):
    name = models.CharField(max_length=250)
    status = models.IntegerField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'college'


class Contactus(models.Model):
    created_at = models.DateTimeField()
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=250)
    phoneno = models.CharField(max_length=10)
    message = models.TextField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'contactus'


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class EmpEducations(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    id = models.BigAutoField(primary_key=True)
    hq_type = models.IntegerField()
    school_medium = models.IntegerField(blank=True, null=True)
    total_marks = models.CharField(max_length=5, blank=True, null=True)
    board = models.ForeignKey(Board, models.DO_NOTHING, blank=True, null=True)
    emp = models.ForeignKey(ApplyEmpInfo, models.DO_NOTHING)
    py = models.ForeignKey('PassingYear', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'emp_educations'


class Empkeyskill(models.Model):
    created_at = models.DateTimeField()
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=50)
    emp = models.ForeignKey(ApplyEmpInfo, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'empkeyskill'


class JobProfile(models.Model):
    created_at = models.DateTimeField()
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    status = models.IntegerField()
    sub_type = models.IntegerField()
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'job_profile'


class PassingYear(models.Model):
    name = models.IntegerField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'passing_year'
