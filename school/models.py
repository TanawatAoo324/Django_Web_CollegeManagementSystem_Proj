from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class TeacherExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    salary = models.PositiveIntegerField(null=False)
    joindate=models.DateField(auto_now_add=True)
    mobile = models.CharField(max_length=40)
    status=models.BooleanField(default=False)
    def __str__(self):
        return self.user.first_name
    @property
    def get_id(self):
        return self.user.id
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name




classes=[('electrical','electrical'),('computer','computer'),('civil','civil'),
('industry','industry'),('chemical','chemical'),('mechanical','mechaincal'),('biology','biology'),('nano','nano'),('aerospace','aerospace'),('energy','energy')]
class StudentExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    roll = models.CharField(max_length=10)
    mobile = models.CharField(max_length=40,null=True)
    fee=models.PositiveIntegerField(null=True)
    cl= models.CharField(max_length=10,choices=classes,default='electrical')
    status=models.BooleanField(default=False)
    profile_pic= models.ImageField(upload_to='images',null=True,blank=True)
    photo = models.ImageField(upload_to="images",blank=True,null=True)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name



class Attendance(models.Model):
    roll=models.CharField(max_length=10,null=True)
    date=models.DateField()
    cl=models.CharField(max_length=10)
    present_status = models.CharField(max_length=10)



class Notice(models.Model):
    date=models.DateField(auto_now=True)
    by=models.CharField(max_length=20,null=True,default='school')
    message=models.CharField(max_length=500)


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    photoprofile = models.ImageField('user-default.png',upload_to='photo_profile',blank=True,null=True)
    usertype = models.CharField(max_length=100,null=True,blank=True,default='student')

    def __str__(self):
        return f'{self.user.username} Profile'

