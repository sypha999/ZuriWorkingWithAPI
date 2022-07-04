from rest_framework import serializers

class LinkSerializer(serialiers.ModelSerializer):
    class Meta:
        model=Link
        fields="__all__"