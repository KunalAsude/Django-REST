from django.db import models
from django.db.models import CASCADE  

class Blog(models.Model):
    blog_name=models.CharField(max_length=100)
    blog_body=models.TextField()


    def __str__(self):
        return self.blog_name
    
class Comment(models.Model):
    blog=models.ForeignKey(Blog,on_delete=CASCADE,related_name='comments')
    comment=models.TextField()

    def __str__(self):
        return self.comment
    
