from django.db import models
from members.models import User

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return "< %s %s>" % (self.user,self.title)
