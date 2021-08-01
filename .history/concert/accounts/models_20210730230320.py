from django.db import models

# Create your models here.

class ProfileModel(models.Model):
                
    class Meta:
        verbose_name="کاربر"
        verbose_name_plural="کاربر"
                
    Name=models.CharField(max_length=100,verbose_name="نام")
    LastName=models.CharField(max_length=100,verbose_name="نام خانوادگی")
    ProfileImage=models.ImageField(upload_to="ProfileImages/",verbose_name="عکس")
                
    Man=1
    Woman=2
    status_choices=(("Man","مرد"),("Woman","زن"))
                
    Gender=models.IntegerField(choices=status_choices,verbose_name="جنسیت")
                
    def __str__(self):
        return "FullName:{} {}".format(Name,LastName)