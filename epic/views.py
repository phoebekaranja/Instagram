from django.http  import HttpResponse
import datetime as dt
# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to the Moringa Tribune')
def convert_dates(dates):
    '''
    function that gets the weekday number of the date.
    '''
    day_number = dt.date.weekday(dates)
    days =['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    '''
    returning the actual day of the week
    '''
    day = days[day_number]
    return day
