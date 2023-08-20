from django.shortcuts import render,redirect
from my_app.froms import TaskForm
from my_app.models import TaskModel
# Create your views here.
def home(request):
    return render( request,'add_tasks.html')

def store_book(request):
    if request.method == 'POST':
        book = TaskForm(request.POST)
        if book.is_valid():
            book.save()
            print(book.cleaned_data)
            return redirect('show_tasks')
            
            
    else:
        book =TaskForm()
    return render (request,'add_tasks.html',{'form':book})

def show_tasks(request):
    book = TaskModel.objects.all()
    print(book)
    return render(request, 'show_tasks.html',{'data':book})

def edit_tasks(request, id):
    task = TaskModel.objects.get(pk=id)
    form = TaskForm(instance=task)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    
    return render(request, 'add_tasks.html', {'form': form})

def delete_book(request, id):
    book = TaskModel.objects.get(pk = id).delete()
    return redirect('show_tasks')
 
def completed_tasks(request):
    tasks = TaskModel.objects.filter(is_completed=True)
    return render(request, 'show_taks.html', {'tasks': tasks})  