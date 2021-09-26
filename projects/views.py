from django.shortcuts import render

from django.http import HttpResponse

project_list=[
                  {"id": 1, "topic": "Making first Django"},
                  {"id":2, "topic": "Rendering data in Django"},
                  {"id":3,"topic":"Making templates inherited and extended"}
             ]

def home(request):
    msg="first"
    num=1   
    context={'message':msg, 'number':num,'project':project_list}
    
    return render(request,'home.html',context )


def projects(request,pk):
    projobj=None
    for i in project_list:
        if i['id']==pk:
            projobj=i
    return render(request,'projects.html',{'project_desc': projobj})
