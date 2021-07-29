from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser

# Create your models here.

class MyUserManger(BaseUserManager):
    def create_user(self,ut_name,prenom,passuser):
        myuser=self.model(ut_name=ut_name,prenom=prenom,passuser=passuser)
        #myuser.set_passuser(passuser)
        myuser.save()
        return myuser
    
"""     def create_superuser(self,ut_name,prenom,passuser,password):
        passuser=make_password(passuser)
        myuser=self.model(ut_name=ut_name,prenom=prenom,passuser=passuser)
        myuser.set_password(password)
        myuser.is_admin=True
        myuser.is_staff=True
        myuser.is_superuser=True
        myuser.save()
 """

class Myuser(AbstractBaseUser):
    ut_name=models.CharField(max_length=100,unique=True)
    prenom=models.CharField(max_length=100,blank=True)
    passuser=models.CharField(max_length=100)
    # joined_on=models.DateTimeField(auto_now_add=True)
    # is_admin=models.BooleanField(default=False)
    # is_active=models.BooleanField(default=True)
    # is_staff=models.BooleanField(default=False)
    # is_superuser=models.BooleanField(default=False)

    objects=MyUserManger()
    USERNAME_FIELD ='ut_name'
    REQUIRED_FIELDS=['prenom','passuser']

    def __str__(self):
        return self.ut_name
    
    # def has_perm(self,perm,obj=None):
    #     return self.is_admin
    # def has_module_perms(self,app_label):
    #     return True
