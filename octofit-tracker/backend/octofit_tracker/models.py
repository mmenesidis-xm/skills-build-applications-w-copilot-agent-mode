from mongoengine import Document, StringField, EmailField, ReferenceField, ListField, IntField, DateTimeField

class User(Document):
    name = StringField(required=True)
    email = EmailField(required=True, unique=True)
    team = StringField()

class Team(Document):
    name = StringField(required=True, unique=True)
    members = ListField(ReferenceField('User'))

class Activity(Document):
    user = ReferenceField('User', required=True)
    type = StringField(required=True)
    duration = IntField(required=True)  # in minutes
    date = DateTimeField(required=True)

class Leaderboard(Document):
    team = ReferenceField('Team', required=True)
    score = IntField(default=0)

class Workout(Document):
    name = StringField(required=True)
    description = StringField()
    suggested_for = ListField(StringField())
