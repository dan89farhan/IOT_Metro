from django.db import models




class Customer(models.Model):
   name = models.CharField(max_length=100, null = False,blank=False)
   uuid = models.IntegerField(primary_key=True,null=False,blank=False)
   contact= models.CharField(max_length=10,null=False,blank=False)
   address=models.CharField(max_length=500,null=False,blank=False)
   status=models.IntegerField(null=False,blank=False)
   finger_print=models.BinaryField(null=False,blank=False)
   

   def __str__(self):
       return str(self.uuid)
    


class Fingerprint_device(models.Model):
   location = models.CharField(max_length=100,null=False,blank=False)
   fid=models.IntegerField(primary_key=True,null=False,blank=False)
   def __str__(self):
       return str(self.fid)


class Wallet(models.Model):
   uuid=models.ForeignKey(Customer, on_delete=models.CASCADE,null=False,blank=False)
   money=models.IntegerField(null=False,blank=False,default=100)
   
   def __str__(self):
       return str(self.uuid)

class LED_bulb(models.Model):
    state = models.BooleanField(default = False,null=False,blank=False)
    
    def __str__(self):
       return 'state'

class Mappingstation(models.Model):
    all_station_name=models.CharField(max_length=20,null=False,blank=False)
    ghatkopar=models.CharField(null=False,blank=False,max_length=20)
    def add_column(self,station_name):
        self.station_name=station_name
        migrations.AddField(
        model_name='Mappingstation',
        name='station_name',
        field=models.CharField( auto_now=True,null=False,blank=False),
        
        ),
    def get_price(self,source,destination):
        self.source=source
        self.destination=destination
        return Mappingstation.objects.filter(destination__all_station_name=source)

    def __str__(self):
        return self.all_station_name

  
class Transaction(models.Model):
    uuid=models.ForeignKey(Customer, on_delete=models.CASCADE,null=False,blank=False)
    source=models.CharField(max_length=20,null=False,blank=False)
    destination=models.CharField(max_length=20,null=False,blank=False)
    fare=models.IntegerField(null=False,blank=False)
    time=models.DateTimeField(auto_now=True,null=False,blank=False)
    status=models.BooleanField(default=False, null=False,blank=False)

 