from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
from django.conf import settings
# Create your models here.


def upload_to(instance,filename):
    return 'user/{filename}'.format(filename=filename)



class UserManager(BaseUserManager):
    def create_user(self, password=None, **extra_fields):
        """
        Creates and saves a User with the given email, name, tc and password.
        """
        user = self.model(
            **extra_fields
        )
        

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email, name, tc and password.
        """
        # user = self.create_user(
        #     email,
        #     password=password,
        #     **extra_fields
        # )
        user = self.model(
            **extra_fields
        )
        user.set_password(password)
        user.is_admin = True
        user.save(using=self._db)
        return user

#  Custom User Model
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
        null=True
    )
    studentId = models.CharField(max_length=50,unique=True,null=True)
    teacherId = models.CharField(max_length=50,unique=True,null=True)



    image = models.ImageField(upload_to=upload_to,default='user/logo.jpg')
    firstname = models.CharField(max_length=50,default="")
    lastname = models.CharField(max_length=50,default="")
    gender = models.CharField(max_length=50,default="")
    classNo =  models.CharField(max_length=20,blank=True)
    religion = models.CharField(max_length=100,default="")
    dob = models.CharField(max_length=12,default="")
    phone = models.CharField(max_length=20,default="")
    admissionNo = models.CharField(max_length=50,default="",blank=True)
    section = models.CharField(max_length=15, default="",blank=True)
    in_class = models.BooleanField(default=False)
    # Parental Details
    fatherName = models.CharField(max_length=50,blank=True)
    fatherOccupation = models.CharField(max_length=50,blank=True)
    fatherMobile = models.CharField(max_length=20,blank=True)
    motherName = models.CharField(max_length=50,blank=True)
    motherOccupation =  models.CharField(max_length=50,blank=True)
    motherMobile = models.CharField(max_length=100,blank=True)
    presentAddress = models.TextField(blank=True)
    permanentAddress = models.TextField(blank=True)


    #Extra Fields for teacher
    qualification =  models.CharField(max_length=50,blank=True)
    experience = models.FloatField(default=0,blank=True)
    education = models.TextField(blank=True)
    certificate = models.TextField(blank=True)
    skills = models.TextField(blank=True)
    department = models.TextField(blank=True)
    
    is_teacher = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self) ->str:
        return str(self.pk)
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

# For Student Details
# class Student(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     image = models.ImageField(upload_to=upload_to,default='user/logo.jpg')
#     firstname = models.CharField(max_length=50,default="")
#     lastname = models.CharField(max_length=50,default="")
#     gender = models.CharField(max_length=50,default="")
#     classNo =  models.CharField(max_length=20,blank=True)
#     religion = models.CharField(max_length=100,default="")
#     dob = models.CharField(max_length=12,default="")
#     phone = models.CharField(max_length=20,default="")
#     admissionNo = models.CharField(max_length=50,default="",blank=True)
#     section = models.CharField(max_length=15, default="",blank=True)
#     # Parental Details
#     fatherName = models.CharField(max_length=50,blank=True)
#     fatherOccupation = models.CharField(max_length=50,blank=True)
#     fatherMobile = models.CharField(max_length=20,blank=True)
#     motherName = models.CharField(max_length=50,blank=True)
#     motherOccupation =  models.CharField(max_length=50,blank=True)
#     motherMobile = models.CharField(max_length=100,blank=True)
#     presentAddress = models.TextField(blank=True)
#     permanentAddress = models.TextField(blank=True)


# # For Teacher Details
# class Teacher(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     image = models.ImageField(upload_to=upload_to,default='user/logo.jpg')
#     name = models.CharField(max_length=50,default="")
#     gender = models.CharField(max_length=50,default="")
#     dob = models.CharField(max_length=12,default="")
#     phone = models.CharField(max_length=20,default="")
#     presentAddress = models.TextField(default="")
#     permanentAddress = models.TextField(default="")
#     qualification =  models.CharField(max_length=50,blank=True)
#     experience = models.FloatField(blank=True)
#     education = models.TextField(blank=True)
#     certificate = models.TextField(blank=True)
#     skills = models.TextField(blank=True)
#     department = models.TextField(blank=True)



class SchoolClass(models.Model):
    name = models.CharField(max_length=50)
    teachers = models.ManyToManyField(User, related_name='classes_taught',blank=True)
    students = models.ManyToManyField(User, related_name='classes_enrolled',blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
