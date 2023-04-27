from django.shortcuts import render

# Create your views here.
import datetime

def built_in_filters(request):
    import datetime
    dt=datetime.datetime.now()
    data={'data':'Hai HELo hoW ArE You','dt':dt,'c':3}
    return render(request,'built_in_filters.html',data)