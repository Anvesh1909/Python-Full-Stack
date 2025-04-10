from rest_framework import serializers
from classBased.models import Friends

class FriendsSeriealizer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        # fields = ['name','phone']
        fields = '__all__'