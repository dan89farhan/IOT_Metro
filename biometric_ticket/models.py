from django.db import models




class Customer(models.Model):
   name = models.CharField(max_length=100)
   uuid = models.IntegerField(primary_key=True)
   contact= models.CharField(max_length=10)
   address=models.CharField(max_length=500)
   finger_print=models.BinaryField()
   
   def __str__(self):
       return self.name


class Fingerprint_device(models.Model):
   location = models.CharField(max_length=100)
   fid=models.IntegerField(primary_key=True)
   def __str__(self):
       return str(self.fid)


class Wallet(models.Model):
   id=models.IntegerField(primary_key=True)
   money=models.IntegerField()
   cust_id=models.ForeignKey(Customer, on_delete=models.CASCADE)
   def __str__(self):
       return self.id

class LED_bulb(models.Model):
    state = models.BooleanField(default = False)
    
    def __str__(self):
       return 'state'
