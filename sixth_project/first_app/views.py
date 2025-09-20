from django.shortcuts import render,redirect
from first_app.forms import StudentForm

# Create your views here.
# def home(request):
#     student=models.Student.objects.all()
#     print(student)
#     return render(request,'home.html',{'data':student})

# def delete_student(request,roll):
#     std=models.Student.objects.get(pk=roll).delete()
#     return redirect("homepage")
def home(request):
    if request.method=='post':
        form=StudentForm(request.post)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    else:
        form=StudentForm()
    return render(request,'home.html',{'form':form})
