from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm ,AuthenticationForm
from .models import *


# class ProposalForm(forms.Form):
#     proposed_project = forms.CharField(label='Proposed Project', max_length=100)
#     student_class = forms.CharField(label='Class', max_length=50)

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'




"""from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm ,AuthenticationForm
from .models import *

"""
# from .models import Student
# from .models import Member

class LoginForm(AuthenticationForm):
    pass


# class StudentLoginForm(AuthenticationForm):
#     pass


# class MemberLoginForm(AuthenticationForm):
#     pass


class ProposalForm(forms.Form):
    proposed_project = forms.CharField(label='Proposed Project', max_length=100)
    student_class = forms.CharField(label='Class', max_length=50)
"""
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    def clean_user(self):
        user = self.cleaned_data.get('user')
        if user is None:
            raise forms.ValidationError("The user field is required.")
        return user


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'

"""

class StudentProposalForm(forms.Form):
    title = forms.CharField(label='Proposed Project', max_length=100)
    desc = forms.Textarea()
    student_class = forms.CharField(label='Class', max_length=50)


# class LoginForm(AuthenticationForm):
#     pass
# class StudentProposalForm(forms.Form):
#     proposed_project = forms.CharField(label='Proposed Project', max_length=100)
#     student_class = forms.CharField(label='Class', max_length=50)

# class StudentForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = '__all__'

#     def clean_user(self):
#         user = self.cleaned_data.get('user')
#         if user is None:
#             raise forms.ValidationError("The user field is required.")
#         return user