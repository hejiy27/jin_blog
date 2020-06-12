from django.db import models
from members.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # hits = models.lntegerField(null=True,blank=True) # 조회수

    def __str__(self):
        return "< %s %s>" % (self.user,self.title)
