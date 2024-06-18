from rest_framework import serializers

class DownloaderSerializer(serializers.Serializer):
    link = serializers.URLField()