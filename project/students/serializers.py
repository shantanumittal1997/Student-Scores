from django.db.models import fields
from rest_framework import serializers

from .models import *

class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = "__all__"

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = "__all__"

    def to_representation(self, instance):

        data = super().to_representation(instance)

        score_qs = Score.objects.filter(student=instance)

        data['scores'] = ScoreSerializer().data if score_qs.exists() else []

        return data

class ScoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Score
        fields = "__all__"