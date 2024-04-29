from django.shortcuts import render, redirect
from django.views import View
from main_app.models.Blood_models import Blood


class Blood_group(View):
    def post(self, request):
        if request.method =="POST":
            name = request.POST.get('name')
            blood_group = request.POST.get('blood')
            phone = request.POST.get('phone')
            alter_phone = request.POST.get('alter_phone')
            facebook = request.POST.get('facebook')
            address = request.POST.get('address')

            users = Blood(name = name, blood_group = blood_group, phone = phone, alter_phone = alter_phone, facebook = facebook, address = address )
            users.save()

        return redirect('blood')

    def get(self, request):
        if 'b' in request.GET:
            b = request.GET['b']
            blood = Blood.objects.filter(blood_group__icontains=b)
            
        else:
           blood = Blood.objects.all()
        
        return render (request, 'blood.html',{'blood': blood})


#         from main_app.models.student_models import Student_info
# from django.shortcuts import render, get_object_or_404



# def Homies(request):
     

# def Person(request, id):
     
#      person = get_object_or_404(Student_info, pk = id)
#      print(person)

#      return render(request, "student.html", {'person':  person})