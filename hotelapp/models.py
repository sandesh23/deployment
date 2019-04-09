from django.db import models

# Create your models here.

class Address(models.Model):
    id = models.AutoField(primary_key=True)
    area = models.TextField(max_length=100,null= False)
    city = models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    country=models.CharField(max_length=100)

class Customer(models.Model):
    address= Address("address")
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    balance = models.IntegerField()
    age = models.IntegerField()
    address = models.ManyToManyField(Address,related_name='address')


class Hotel(models.Model):
    id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=100)
    rating = models.CharField(max_length=100)
    branch_name = models.CharField(max_length=100)
    address=models.OneToOneField(Address,on_delete=models.CASCADE)
    balance = models.IntegerField()
    costToBusiness= models.IntegerField()
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)

'''This line is added by another developer'''
class Waiter(models.Model):
    aadharNo = models.BigIntegerField(primary_key=True)
    name= models.CharField(max_length=100)
    age=models.IntegerField()
    qualification = models.CharField(max_length=100)
    salary=models.IntegerField()
    category=models.TextField(max_length=100)
    address=models.OneToOneField(Address,on_delete=models.CASCADE)


class Manager(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age=models.IntegerField()
    address = models.OneToOneField(Address,on_delete=models.CASCADE)
    qualification = models.CharField(max_length=100,null=False)
    salary = models.IntegerField()
    Hotel = models.OneToOneField(Hotel,on_delete=models.CASCADE)
    waiter=models.ForeignKey(Waiter,on_delete=models.CASCADE)



class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    vegDishPrice=models.IntegerField()
    nonVegDishPrice = models.IntegerField()
    chineseDishPrice = models.IntegerField()
    dessertPrice = models.IntegerField()
    starterPrice=models.IntegerField()
    hotel=models.ManyToManyField(Hotel)





