from rest_framework import serializers

from hapifakenews.models import FakeSite


# Serializers define the API representation.
class FakeSiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FakeSite
        fields = ('site', 'url', 'source', 'sourceurl', 'isfake', 'since')


