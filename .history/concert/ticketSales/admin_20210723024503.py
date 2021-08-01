from django.contrib import admin
from .models import concertModel
from .models import locationModel
from .models import  timeModel
from .models import  ProfileModel
from .models import  ticketModel

# Register your models here.

admin.site.register(concertModel)
admin.site.register(locationModel)
admin.site.register(timeModel)
admin.site.register(ProfileModel)
admin.site.register(ticketModel)

