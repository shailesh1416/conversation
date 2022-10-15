from django.db import models

# Create your models here.


class Conversation(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Chats(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    sentence = models.TextField(max_length=500)
    voice_record = models.FileField(upload_to="records")
    sentence_no = models.FloatField(blank=False,default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + "=>" + str(self.sentence)
