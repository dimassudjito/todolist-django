from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .models import Task
from .forms import TaskForm, DoneForm


# Creating list view
# def list_view(request):
#     queryset = Task.objects.all()#creates a list from object database
#     context = {
#         'object_list': queryset #create keyword to call the list
#     }
#     return render(request,"list/task_list.html",context)

# # Create list view 2.0
# def list_view(request):
#     queryset = Task.objects.all()#creates a list from object database
#     form = TaskForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = TaskForm()
#     context = {
#         'object_list': queryset, #create keyword to call the list
#         'form': form
#     }
#     return render(request,"list/task_list.html",context)

# Create list view 3.0
def list_view(request):
    queryset = Task.objects.all() # creates a list from object database
    form = TaskForm(request.POST or None) # create a form
    # done_form = DoneForm(request.POST or None)

    if form.is_valid(): # executing form
        form.save()
        form = TaskForm()

    # if done_form.is_valid():
    #     obj = done_form.save(commit=False)
    #     obj.done = True
    #     obj.save()

    context = {
        'object_list': queryset,
        'form': form,
        # 'done_form': done_form,
    }
    return render(request,"list/task_list.html",context)

# Creating create view
# def list_create_view(request):
#     form = TaskForm(request.POST or None)#check if there's POST request or not
#     if form.is_valid(): #check if input is valid
#         form.save()#save it to database
#         form = TaskForm()#refresh the form
#     context = {
#         'form': form
#     }
#     return render(request,"list/task_create.html",context)

# Create delete view
# def list_delete_view(request, id):
#     obj = get_object_or_404(Task, id=id,)
#     if request.method == "POST": #checking if method is POST
#         obj.delete() #confirm deleting the object
#         return redirect('../') #redirect the page after deleting the object
#     context = {
#         'object' : obj
#     }
#     return render(request,"list/task_delete.html",context)

# Creating delete function
def list_delete_view(request, id):
    obj = Task.objects.get(id=id)
    obj.delete()
    return HttpResponseRedirect('/list/')

# # Create done function
# def list_done_view(request, id):
#     if form.is_valid():
#         obj = form.save(commit=False)
#         obj.done = True
#         obj.save()
#         return redirect('/list/')




