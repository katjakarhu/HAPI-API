from rest_framework import serializers

from hapisentiment.models import SentimentData


class SentimentDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SentimentData
        fields = ('text', 'url', 'isFake')