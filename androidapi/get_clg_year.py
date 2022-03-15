#that file used for getting college name and passing year

from androidapi.models import Board, College,PassingYear
def getallcollege():
    try:
        college=College.objects.filter(status=1)
        return college
    except Exception as e :
        pass

def getallpassingyear():
    try:
        passing=PassingYear.objects.all()
        return passing
    except Exception as e :
        pass

def getallboard():
    try:
        passing=Board.objects.all()
        return passing
    except Exception as e :
        pass    
