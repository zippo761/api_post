from rest_framework import serializers
from .models import Article

# Реализуем сериализитор используя ModelSerializer в котором уже реализован create update
# и набор валидаторов по умолчанию


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model =  Article
        fields = ('id', 'title', 'description', 'body', 'author_id')
