from django.shortcuts import render
from populate_firsst_app import AccessRecord, Topic, Webpage

# Create your views here.
def home(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    return render(request,'first_app/index.html',date_dict)
