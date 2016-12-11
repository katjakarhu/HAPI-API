from rest_framework import serializers

from hapifakenews.models import FakeSite


# Serializers define the API representation.
class FakeSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FakeSite
        fields = ('id', 'name', 'url', 'language', 'source_name', 'source_url', 'source_extra_info', 'comment_from_api', 'created', 'created_by', 'updated')


