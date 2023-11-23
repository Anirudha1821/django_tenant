from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from .models import project_name

def index(request):
    print("-------",request.tenant,"------------")
    # return HttpResponse(f"<h1>This is {request.tenant}  indexsssssssssss page </h1> ")
    project_names=project_name.objects.all()
    return render(request, 'client_index.html',{"projects":project_names})

def create_project(request):
    if(request.method == 'POST'):
        name = request.POST.get("name")
        new_project=project_name(name=name)
        new_project.save()
        return redirect("client_index")
    # return HttpResponse(f"<h1>{request.tenant} New {name} project  added </h1> ")