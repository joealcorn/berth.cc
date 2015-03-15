from rest_framework import serializers


class GithubWebhookSerializer(serializers.Serializer):
    repository = serializers.DictField()
    hook = serializers.DictField()
    sender = serializers.DictField()
