from rest_framework import serializers
from snippet.models import snippet

class SnippetSerializer(serializers.HyperlinkedModelSerializer)