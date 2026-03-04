from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from octofit_tracker.serializers import (
    UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
)

class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    def retrieve(self, request, pk=None):
        user = User.objects(id=pk).first()
        if not user:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Response(serializer.data)

class TeamViewSet(viewsets.ViewSet):
    def list(self, request):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)
    def retrieve(self, request, pk=None):
        team = Team.objects(id=pk).first()
        if not team:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TeamSerializer(team)
        return Response(serializer.data)

class ActivityViewSet(viewsets.ViewSet):
    def list(self, request):
        activities = Activity.objects.all()
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)
    def retrieve(self, request, pk=None):
        activity = Activity.objects(id=pk).first()
        if not activity:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ActivitySerializer(activity)
        return Response(serializer.data)

class LeaderboardViewSet(viewsets.ViewSet):
    def list(self, request):
        leaderboards = Leaderboard.objects.all()
        serializer = LeaderboardSerializer(leaderboards, many=True)
        return Response(serializer.data)
    def retrieve(self, request, pk=None):
        leaderboard = Leaderboard.objects(id=pk).first()
        if not leaderboard:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = LeaderboardSerializer(leaderboard)
        return Response(serializer.data)

class WorkoutViewSet(viewsets.ViewSet):
    def list(self, request):
        workouts = Workout.objects.all()
        serializer = WorkoutSerializer(workouts, many=True)
        return Response(serializer.data)
    def retrieve(self, request, pk=None):
        workout = Workout.objects(id=pk).first()
        if not workout:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = WorkoutSerializer(workout)
        return Response(serializer.data)
