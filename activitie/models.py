from django.db import models
from django.core.urlresolvers import reverse

class Quiz(models.Model):
    quizTitle = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    matter = models.CharField(max_length=250)
    #quizImage = models.CharField(max_length=1000)
    quizImage = "https://cdn0.iconfinder.com/data/icons/flatico/512/monitor_code__editor-512.png"


    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.quizTitle + ' - ' + self.matter

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    fileType = models.CharField(max_length=4)
    QuesTitle = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    Questiontext = models.TextField(max_length=None)
    is_Done = models.BooleanField(default=False)

    def __str__(self):
        return self.QuesTitle
