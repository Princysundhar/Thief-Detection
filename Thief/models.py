from django.db import models

# Create your models here.


class login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    type = models.CharField(max_length=50)

class crime_category(models.Model):
    category_name = models.CharField(max_length=100)

class police_station(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)

    LOGIN = models.ForeignKey(login, on_delete=models.CASCADE, default=1)

class criminals(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    id_proof = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)


    CATEGORY = models.ForeignKey(crime_category,on_delete=models.CASCADE,default=1)
    POLICE = models.ForeignKey(police_station,on_delete=models.CASCADE,default=2)




class user(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    # id_proof = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(login, on_delete=models.CASCADE, default=1)

class camera(models.Model):
    camera_number = models.CharField(max_length=20)
    USER  = models.ForeignKey(user,on_delete=models.CASCADE,default=1)

class alert(models.Model):
    date = models.CharField(max_length=100)
    CAMERA = models.ForeignKey(camera,on_delete=models.CASCADE,default=1)
    CRIMINALS = models.ForeignKey(criminals,on_delete=models.CASCADE,default=1)

class familiar_person(models.Model):
    F_name = models.CharField(max_length=100)
    F_place = models.CharField(max_length=100)
    F_email = models.CharField(max_length=100)
    F_contact = models.CharField(max_length=100)
    # F_lattitude = models.CharField(max_length=100)
    # F_longitude = models.CharField(max_length=100)
    F_image = models.CharField(max_length=100)
    USER = models.ForeignKey(user, on_delete=models.CASCADE, default=1)

class visitor_log(models.Model):
    image = models.CharField(max_length=200)
    date = models.CharField(max_length=100)
    time  = models.CharField(max_length=100)
    CAMERA = models.ForeignKey(camera,on_delete=models.CASCADE,default=1)

class familiar_log(models.Model):
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    FAMILIAR_PERSON = models.ForeignKey(familiar_person,on_delete=models.CASCADE,default=1)


