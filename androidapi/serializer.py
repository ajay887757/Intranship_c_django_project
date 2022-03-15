from rest_framework import serializers
from adminweb.models import District, State

from androidapi.models import JobCode, Applied, ApplyEmpInfo, Appversion, Board,College, EmpEducations, EmpkeySkill, Job_profile,PassingYear, Stream_type, TIPActivationCode

class JobCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCode
        fields = '__all__'

class college_codeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = '__all__'
class PassingYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassingYear
        fields = '__all__'        

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'                
class PySerializer(serializers.ModelSerializer): #passing year
    class Meta:
        model = PassingYear
        fields = '__all__'    

class BoardSerializer(serializers.ModelSerializer): #passing year
    class Meta:
        model = Board
        fields = '__all__'

class keySkillsSerializer(serializers.ModelSerializer): #passing year
    class Meta:
        model = EmpkeySkill
        fields = '__all__'        

        
class ApplyempSerializer(serializers.ModelSerializer): #passing year

    class Meta:
        model = ApplyEmpInfo
        fields = '__all__' 
class StreamSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Stream_type
        fields = '__all__'
                          
class EmpinfoSerializer(serializers.ModelSerializer):
    passing_year=PySerializer()
    college=college_codeSerializer()
    course_type=StreamSerializer()

    class Meta:
        model = ApplyEmpInfo 
        fields = '__all__'   
        extra_fields =['college','passing_year','course_type']          
class EmpEduSerializer(serializers.ModelSerializer): 
    py=PySerializer()
    # emp=ApplyempSerializer()
    board=BoardSerializer()
    class Meta:
        model = EmpEducations
        fields = '__all__'   
        extra_fields =['py','board']     
class JobprofileSerializer(serializers.ModelSerializer): 

    class Meta:
        model = Job_profile
        fields = '__all__' 

class AppliedSerializer(serializers.ModelSerializer): 
    jobprofile=JobprofileSerializer()
    class Meta:
        model = Applied
        fields = '__all__'
        extra_fields =['jobprofile']            


class AppversionSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Appversion
        fields = '__all__'


#Tip serializer
class TipActivationcodeserilizer(serializers.ModelSerializer): 
    class Meta:
        model = TIPActivationCode
        fields = '__all__'
class State_serilizer(serializers.ModelSerializer): 
    class Meta:
        model = State
        fields = '__all__'
class District_serilizer(serializers.ModelSerializer): 
    class Meta:
        model = District
        fields = '__all__'

