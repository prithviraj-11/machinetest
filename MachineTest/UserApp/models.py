from django.db import models

# Create your models here.
class UserInfo(models.Model):
    id=models.AutoField(auto_created=True,primary_key=True)
    first_name=models.CharField(max_length=10,default='')
    last_name=models.CharField(max_length=10,default='')
    email=models.EmailField(max_length=50)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=10)
    phone_number=models.IntegerField(default='')
    role=models.CharField(max_length=20,default='User')

    class Meta:
        db_table="UserInfo"


        