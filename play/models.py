from django.db import models

# Create your models here.
class Paper(models.Model):
    paper = models.CharField(max_length=200)
    which_state = models.CharField(max_length=200)
    year = models.IntegerField()
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.paper

class Question(models.Model):
    question = models.CharField(max_length=200)
    paper = models.ForeignKey(Paper)
    file_path = models.FileField(upload_to="video")
    def __unicode__(self):
        return self.question
    