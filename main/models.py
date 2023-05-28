from datetime import timedelta, datetime, timezone
from typing import AbstractSet
from django.db import models
from django.contrib.auth  import get_user_model
# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_member = models.BooleanField(default=False)
    
class Userpro(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255,null=True)
    email = models.EmailField(null=True)
    roll_number = models.CharField(max_length=50,null=True)
    last_login = models.DateTimeField(auto_now=False, auto_now_add=False,null=True)
    profile_pic = models.CharField(max_length=250,null=True)

    def __str__(self):
        return self.name

class Member(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255,null=True)
    email = models.EmailField(null=True)
    role = models.CharField(max_length=100, null=True)
    last_login = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)

    def __str__(self):
        return self.name
    
class Proposal(models.Model):
    title = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    student = models.ForeignKey('Student', related_name='student_table', on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True, null=True)
    class_field = models.CharField(max_length=100,null=True)
    section = models.CharField(max_length=10,null=True)
    semester = models.CharField(max_length=10,null=True)
    number_of_students = models.IntegerField(null=True)
    status = models.CharField(max_length=250, default='pending')
    comments = models.CharField(max_length=250,null=True)
    presentation = models.DateTimeField(null=True)
    student_names = models.CharField(max_length=250,null=True)
    student_rolls = models.CharField(max_length=250,null=True)
    student_sections = models.CharField(max_length=250,null=True)
    
class ProposalReview(models.Model):
    teacher = models.ForeignKey('Member', related_name='student_table', on_delete=models.CASCADE)
    proposal = models.ForeignKey('Proposal', on_delete=models.CASCADE)
    review = models.TextField(null=True)
    datetime = models.DateTimeField(auto_now_add=True, null=True)
    
    def get_due_date(self):
        if self.datetime:
            return datetime.strptime(self.datetime) + timedelta(weeks=1)
        else:
            return ''
    
class Notication(models.Model):
    title = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)
