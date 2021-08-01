from django.db import models

# Create your models here.

class concertModel(models.Model):
    Name=models.CharField(max_length=100)
    SingerName=models.CharField(max_length=100)
    length=models.IntegerField()
    
    def __str__(self):
        return self.SingerName
    
    
    class locationModel(models.Model):
        IdNumber=models.IntegerField(primary_key=True)
        Name=models.CharField(max_length=100)
        Address=models.CharField(max_length=500,default="Tehran-Milad Tower")
        Phone=models.CharField(max_length=11,null=True)
        Capacity=models.IntegerField()
        
        def __str__(self):
            return self.Name
        
        
        class timeModel(models.Model):
            concertModel=models.ForeignKey('concertModel',on_delete=models.PROTECT)
            locationModel=models.ForeignKey('locationModel',on_delete=models.PROTECT)
            StartDateTime=models.DateTimeField()
            Seats=models.IntegerField()
            