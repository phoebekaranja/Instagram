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
def image_today(request):
    epic = Image.gallery_images()
    category= Categorys.objects.all()
    location= Location.objects.all()
    return render(request,'all-images/gallery-images.html',{"epic":epic,'category':category,"location":location})
def search_results(request):
    category= Categorys.objects.all()
    location= Location.objects.all()
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_image = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-images/search.html',{"message":message,"images": searched_image,'category':category,"location":location})    
