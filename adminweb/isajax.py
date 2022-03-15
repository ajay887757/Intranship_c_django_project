import calendar
from datetime import *

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
def get_month_max(year,month):
    last_day=calendar.monthrange(year, month)[1]
    return datetime(year,month,last_day,23,59,59)

