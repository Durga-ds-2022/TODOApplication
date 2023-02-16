from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
context={}
# Create your views here.
def home(request):
    if request.method=="POST":
        name= request.POST['name']
        obj= Todo.objects.create(name= name)
        return redirect('/')
    context['todo']= Todo.objects.all()    
    return render(request, 'home.html', context)


def delete_todo(request, id):
    try:
        todo_obj = Todo.objects.get(id= id).delete()
    except Exception as e:
        print(e)
    return redirect('home')     

def update_todo(request):
    id= request.GET.get('id')    
    try:
        todo_obj = Todo.objects.get(id= id)
        todo_obj.is_completed= not todo_obj.is_completed
        todo_obj.save()
    except Exception as e:
        print(e)
    return redirect('home')     