from django.contrib import admin
from .models import CustomUser, Notication, Proposal, ProposalReview, Student,Member
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'roll_number']

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'role']

admin.site.register(CustomUser)
admin.site.register(Proposal)
admin.site.register(ProposalReview)
admin.site.register(Notication)
# # admin.site.register(Member, MemberAdmin)