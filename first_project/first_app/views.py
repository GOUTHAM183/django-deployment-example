from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
'''def index(request):
    dict1 = {'goutham' : "HELLO MAY I HELP YOU!!"}
    return render(request,'help.html',context=dict1)'''

def help(request):
    helpdic = {'goutham':"HELLO!! RTY"}
    return render(request,'first12/help.html',context=helpdic)
