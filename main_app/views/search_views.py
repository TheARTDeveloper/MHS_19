from main_app.models.student_models import Student_info
from django.shortcuts import render, get_object_or_404



def Homies(request):
     if 'q' in request.GET:
            q = request.GET['q']
            student_data = Student_info.objects.filter(name__icontains=q)
            
     else:
        student_data = Student_info.objects.all()
        

     return render(request, 'student_info.html', {'student_data':student_data})

def Person(request, id):
     
     person = get_object_or_404(Student_info, pk = id)
     print(person)

     return render(request, "student.html", {'person':  person})