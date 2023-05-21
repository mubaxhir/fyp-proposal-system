from django.contrib.auth.backends import ModelBackend
from .models import Student, Member

class StudentBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            student = Student.objects.get(user__username=username)
            if student.user.check_password(password):
                return student.user
        except Student.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Student.objects.get(id=user_id)
        except Student.DoesNotExist:
            return None

class MemberBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            member = Member.objects.get(user__username=username)
            if member.user.check_password(password):
                return member.user
        except Member.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Member.objects.get(id=user_id)
        except Member.DoesNotExist:
            return None
