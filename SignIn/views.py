from django.shortcuts import render
from SignIn.forms import StudentForm
from django.views.decorators.http import require_POST, require_http_methods
from django.http import JsonResponse

@require_http_methods(['GET'])
def index(request):
    form = StudentForm()

    context = {'form': form}
    return render(request, 'SignIn/Index.html', context)

@require_POST
def create_student(request):
    newStudent = StudentForm(request.POST)
    print(newStudent.errors)
    if newStudent.is_valid():
        data = {'student_is_valid': True}
        newStudent.save()
        return JsonResponse(data)
    else:
        data = {'student_is_valid': False}
        return JsonResponse(data)

