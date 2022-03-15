
from django.http import HttpResponse
from androidapi.models import ApplyEmpInfo,College as Cg, Job_profile,PassingYear, Stream_type
from adminweb.models import Surveyinfo

def create(request):

    Surveyinfodata=Surveyinfo.objects.using("CRTD-RC"). all()
    for surveyor in Surveyinfodata:
        if surveyor.survey_info_id!=1 and surveyor.survey_info_id!=2:
            pydata={
                1:"2021",
                2:"2022"
            }
            jobid=Job_profile.objects.get(id=17)
            streamtype=Stream_type.objects.get(id=surveyor.highqualification)
            print(surveyor.college_name)
            cgid=Cg.objects.get(id=surveyor.college_name)
            # pyid=PassingYear.objects.get(name=pydata[surveyor.passing_year])
            # ApplyEmpInfo.objects.create(longitude=surveyor.current_longitude,lattitude=surveyor.current_lattitude,gender=0,name=surveyor.survey_name,phoneno=surveyor.survey_id.survey_mobile,whphoneno=surveyor.survey_id.survey_mobile,email=surveyor.survey_id.survey_email,password=surveyor.survey_id.password,course_type=streamtype,college=cgid,passing_year=pyid,branch=None,photo=surveyor.survey_profile_image,created_at=surveyor.created_at,updated_at=surveyor.updated_at,profile_status=0,fullsizephoto="",paddress=surveyor.survey_address,caddress=surveyor.survey_address,regid=surveyor.survey_id.survey_registration_id,loginpin=surveyor.survey_id.survey_code_pin,referal_code='CRTDHRRU10',selected_job_profile=jobid)

    # allcollege=College.objects.using("CRTD-RC").all()
    # for college_d in allcollege:
    #     if college_d.id!=26:
    #         Cg.objects.create(name=college_d.name,status=college_d.status,created_at=college_d.created_at)
    # id=4
    # collegedata=Cg.objects.all()
    # for college_d in collegedata:
    #         if college_d.id>29:
    #             Surveyinfo.objects.using("CRTD-RC").filter(college_name=id).update(college_name=college_d.id)
    #             id=id+1



    return HttpResponse("done")

