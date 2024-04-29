from django.db import models

class SocialWork(models.Model):
   
    image = models.ImageField(upload_to='image/%y', blank = True)
    details = models.CharField(max_length= 230, blank=True)


    def __str__(self):
        return self.details

    # @staticmethod
    # def get_social_work():
    #     return SocialWork.objects.all()