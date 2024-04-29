from django.shortcuts import render
from django.views import View
from main_app.models.Home_models import Home
from main_app.models.socialWork_models import SocialWork
from main_app.models.student_models import Student_info

class Home_items(View):
    def post(self, request):
        return render (request, 'base.html')
    
    def get(self, request):

         if 'q' in request.GET:
            q = request.GET['q']
            student_data = Student_info.objects.filter(name__icontains=q)
            
         else:
            student_data = Student_info.objects.all()

         home_data = Home.get_all_home_items()
         social_work = SocialWork.objects.all()
         student_data = Student_info.objects.all()

         return render(request,'base.html', {'home_data': home_data , 'social_work': social_work, 'student_data': student_data})

   


