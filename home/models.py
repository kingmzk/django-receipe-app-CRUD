from django.db import models

# Create your models here.

class Student(models.Model):
   # id = models.AutoField()                      #By default django will add this field
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    adress = models.TextField()
    # image = models.ImageField()
    # file = models.FileField()
    
    
class Car(models.Model):
    car_name = models.CharField(max_length=20)
    speed = models.IntegerField(default=100)

    def __str__(self) -> str:
        return f"{self.car_name} {str(self.speed)}"
       #return self.car_name + " " + str(self.speed)


    