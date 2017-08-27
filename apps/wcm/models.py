from django.db import models
from django.contrib.auth.models import User

class Period(models.Model):
    name = models.CharField(max_length=20)
    sort_no = models.IntegerField()
    ins_at = models.DateTimeField(auto_now_add=True)
    upd_at = models.DateTimeField(auto_now=True)

STATUS = (
    ('first','作成中'),
    ('second','上長コメント中'),
    ('exe','実践中'),
    ('eval','振り返り'),
    ('end','終了'),
)
class Status(models.Model):
    name = models.CharField(max_length=20)
    sort_no = models.IntegerField()
    status_type = models.CharField(max_length=5, choices=STATUS)

class Sheet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    ins_at = models.DateTimeField(auto_now_add=True)
    upd_at = models.DateTimeField(auto_now=True)

class Will(models.Model):
    sheet = models.ForeignKey(Sheet, on_delete=models.CASCADE)
    realize_member = models.TextField()
    realize_manager = models.TextField()
    career_image_member = models.TextField()
    career_image_manager = models.TextField()

class Can(models.Model):
    sheet = models.ForeignKey(Sheet, on_delete=models.CASCADE)
    strength_member = models.TextField()
    strength_manager = models.TextField()
    weekness_member = models.TextField()
    weekness_manager = models.TextField()
    action = models.TextField()
    evaluation = models.TextField()

class Must(models.Model):
    sheet = models.ForeignKey(Sheet, on_delete=models.CASCADE)
    thema = models.TextField()
    content = models.TextField()
    evaluation = models.TextField()
    score_member = models.IntegerField()

class MustMission(models.Model):
    must = models.ForeignKey(Must, on_delete=models.CASCADE)
    goal = models.TextField()
    process = models.TextField()
    to_report = models.TextField()
    score_member = models.IntegerField()
    criteria = models.TextField()
    weight = models.IntegerField()
    result = models.TextField()
    score_member = models.IntegerField()
    score_manager = models.IntegerField()
