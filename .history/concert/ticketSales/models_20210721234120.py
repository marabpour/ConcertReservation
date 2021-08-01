from django.db import models

# Create your models here.

class concertModel(models.Model):
    Name=models.CharField(max_length=100)
    SingerName=models.CharField(max_length=100)
    length=models.IntegerField(default =0)
    
    def __str__(self):
        return self.SingerName
    
    
    class locationModel(models.Model):
        IdNumber=models.IntegerField(primary_key=True)
        Name=models.CharField(max_length=100)
        Address=models.CharField(max_length=500,default="تهران-برج میلاد")
        Phone=models.CharField(max_length=11,null=True)
        Capacity=models.IntegerField()
        
        def __str__(self):
            return self.Name
        
        
        class timeModel(models.Model):
            Concert= models.ForeignKey(concertModel,on_delete=models.PROTECT)
            Location= models.ForeignKey(locationModel,on_delete=models.PROTECT)
            StartDateTime= models.DateTimeField()
            Seats= models.IntegerField()
            