from main.models import Proposal, Student
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class ProposalSerializer(serializers.ModelSerializer):
    student = StudentSerializer()  # Use the StudentSerializer for the student field

    class Meta:
        model = Proposal
        fields = '__all__'