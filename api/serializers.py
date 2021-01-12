from django_starter_app.models import *
from django.contrib.auth.models import User
from rest_framework import serializers


# class WordSerializer(serializers.ModelSerializer):
# 	word_translation = serializers.CharField(source='station.name', read_only=True)
# 	class Meta:
# 		model = Word
# 		fields = ['id', 'word', 'word_translation']

# class LanguageSerializer(serializers.ModelSerializer):
# 	language_translation = serializers.RelatedField(many=True, read_only=True)
# 	word_translation = serializers.RelatedField(many=True)
# 	class Meta:
# 		model = LanguageName
# 		fields = ['id', 'name',  'word_translation']



# class TranslationSerializer(serializers.ModelSerializer):
#     words = WordSerializer(many=True, read_only=True)
#     language_translation = LanguageSerializer(many=True, read_only=True)
#     class Meta:
#         model = Translation
#         fields = [  'id',
# 					'description',
#                     'words',
#                     'language_translation'
# 				]






