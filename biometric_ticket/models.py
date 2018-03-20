from django.db import models




class customer(models.Model):
   name = models.CharField(max_length=100)
   uuid = models.IntegerField(primary_key=True)
   contact= models.CharField(max_length=10)
   address=models.CharField(max_length=500)
   finger_print=models.BinaryField()


class fingerprint_device(models.Model):
   location = models.CharField(max_length=100)
   fid=models.IntegerField(primary_key=True)


class wallet(models.Model):
   id=models.IntegerField(primary_key=True)
   money=models.IntegerField()
   cust_id=models.ForeignKey(customer, on_delete=models.CASCADE)
