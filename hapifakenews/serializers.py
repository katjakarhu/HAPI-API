from rest_framework import serializers

from hapifakenews.models import FakeSite


# Serializers define the API representation.
class FakeSiteSerializer(serializers.Serializer):
    class Meta:
        model = FakeSite
        fields = ('name', 'url', 'sourcename', 'sourceurl', 'ratingatsource', 'created', 'createdby', 'updated')


