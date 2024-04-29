from django.db import models

class Home(models.Model):
    headline = models.CharField(max_length= 100,  blank = True)
    details = models.CharField(max_length= 230,  blank = True)
    image = models.ImageField(upload_to= 'image/%y', blank = True)


    def __str__(self):
        return self.headline

    @staticmethod
    def get_all_home_items():
        return Home.objects.all()