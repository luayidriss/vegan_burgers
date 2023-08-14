from rest_framework import serializers

class TotalGuestsSerializer(serializers.Serializer):
    total_guests = serializers.IntegerField()