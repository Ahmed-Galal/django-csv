from rest_framework import serializers

from ..models.usercsv import Usercsv


class UserCSVSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usercsv
        fields = (
            "id", "title", "description","image"
        )
