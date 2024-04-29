from django.contrib import admin

from .models.student_models import Student_info 
from .models.Home_models import Home
from .models.socialWork_models import SocialWork
from .models.Blood_models import Blood


admin.site.register(Home)
admin.site.register(SocialWork)



@admin.register(Student_info)
class StudentInfo(admin.ModelAdmin):
    list_display =('name','image' ,'facebook', 'email','phone', 'blood', 'detail')
    list_filter = ('name', 'phone', 'blood')
    search_fields = ('name','phone', 'blood')


@admin.register(Blood)
class BloodAdmin(admin.ModelAdmin):
    list_display =('name','facebook','phone', 'blood_group', 'address')
    list_filter = ('name','blood_group')
    search_fields = ('name', 'blood_group')
