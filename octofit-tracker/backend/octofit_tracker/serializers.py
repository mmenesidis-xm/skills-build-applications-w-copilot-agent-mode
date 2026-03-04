from rest_framework import serializers
from octofit_tracker import models

class UserSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField()
    email = serializers.EmailField()
    team = serializers.CharField()

class TeamSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField()
    members = serializers.ListField(child=serializers.CharField(), required=False)

class ActivitySerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    user = serializers.CharField()
    type = serializers.CharField()
    duration = serializers.IntegerField()
    date = serializers.DateTimeField()

class LeaderboardSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    team = serializers.CharField()
    score = serializers.IntegerField()

class WorkoutSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    suggested_for = serializers.ListField(child=serializers.CharField())
