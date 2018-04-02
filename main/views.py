from django.shortcuts import render

# Create your views here.


def index(request):
   return render(request,'contacts.html')

def calendar(request):
    return  render(request, 'calendar.html')

def assistants(reqeust):
    return  render(reqeust, 'assistants.html')

def reports(request):
    return render(request, 'reports.html')