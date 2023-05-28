import datetime
from django.contrib import admin
from .models import CustomUser, Notication, Proposal, ProposalReview, Student,Member
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'roll_number']

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'role']
    
    
# Define a function that will update the values.
def update_values(obj):
    queryset = Proposal.objects.all()
    start_time = obj.presentation

    for object in queryset:
        start_time = start_time + datetime.timedelta(minutes=15)
        object.presentation = start_time
        object.save()

    queryset.update()
    return obj

# Override the `save_model()` method of the ModelAdmin class.
class ProposalAdmin(admin.ModelAdmin):
  def save_model(self, request, obj, form, change):
    # Call the function to update the values.
    obj = update_values(obj)

    super().save_model(request, obj, form, change)

admin.site.register(CustomUser)
admin.site.register(Proposal, ProposalAdmin)
admin.site.register(ProposalReview)
admin.site.register(Notication)
# # admin.site.register(Member, MemberAdmin)