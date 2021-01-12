from django.db import models

# Create your models here.


class LanguageName(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Word(models.Model):
    word = models.CharField(max_length=100)
    language_id = models.ForeignKey(LanguageName, related_name='words', on_delete=models.CASCADE)

    def __str__(self):
        return self.word

class Translation(models.Model):
    word_id = models.ForeignKey(
        Word, related_name='word_translation',  on_delete=models.CASCADE)
    language_id = models.ForeignKey(
        LanguageName, related_name='language_translation',  on_delete=models.CASCADE)
    description = models.TextField()
    
    def __str__(self):
        return 'Translation '+str(self.word_id.word)
