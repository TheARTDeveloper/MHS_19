from django.db import models

class Blood(models.Model):
    name = models.CharField(max_length= 30)
    blood_group = models.CharField(max_length= 20)
    phone = models.CharField(max_length= 20)
    alter_phone = models.CharField(max_length= 20, blank=True, default="N/A")
    address = models.TextField(max_length= 440 )
    facebook = models.TextField(max_length=440, blank=True)


    def __str__(self):
        return self.name