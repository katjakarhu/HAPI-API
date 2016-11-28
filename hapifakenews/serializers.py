from rest_framework import serializers

from hapifakenews.models import FakeNews, FakeSite


# Serializers define the API representation.
class FakeNewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FakeNews
        fields = ('url', 'name', 'source', 'isfake')

class FakeSiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FakeSite
        fields = ('site')

