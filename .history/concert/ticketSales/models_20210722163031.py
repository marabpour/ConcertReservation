from django.db import models

# Create your models here.


class concertModel(models.Model):
    Name=models.CharField(max_length=100)
    SingerName=models.CharField(max_length=100)
    length=models.IntegerField()
    test=models.CharField(max_length=10,null=True)
    Poster=models.ImageField(upload_to="ConcertImages/",null=True)
    
    
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
            concertModel=models.ForeignKey('concertModel',on_delete=models.PROTECT)
            locationModel=models.ForeignKey('locationModel',on_delete=models.PROTECT)
            StartDateTime=models.DateTimeField()
            Seats=models.IntegerField()
            
            
            Start=1
            End=2
            Cancel=3
            Sales=4
            status_choices=(("Start","فروش بلیط شروع شده است"),
                           ("End","فروش بلیط تمام شده است"),
                           ("Cancel","این سانس کنسل شده است"),
                           ("Sales","در حال فروش بلیط"))
            
            Status=models.IntegerField(choices=status_choices)
            
            def __str__(self):
                return "Time: {} concertName: {} Location: {}".format(StartDateTime,concertModel.Name,locationModel.Name)
            
            
            class ProfileModel(models.Model):
                Name=models.CharField(max_length=100)
                LastName=models.CharField(max_length=100)
                ProfileImage=models.ImageField(upload_to="ProfileImages/")
                
                Man=1
                Woman=2
                status_choices=(("Man","مرد"),("Woman","زن"))
                
                Gender=models.IntegerField(choices=status_choices)
                
                def __str__(self):
                    return "FullName:{} {}".format(Name,LastName)
                
                class ticketModel(models.Model):
                    ProfileModel=models.ForeignKey('ProfileModel',on_delete=models.PROTECT)
                    timeModel=models.ForeignKey("timeModel",on_delete=models.PROTECT)
                    TicketImage=models.ImageField(upload_to="TicketImages/")
                    Name=models.CharField(max_length=100)
                    Price=models.IntegerField()
                    
                    def __str__(self):
                        return "TicketInfo: Profile: {} ConcertInfo : {}".format(timeModel.__str__())
                    
                                