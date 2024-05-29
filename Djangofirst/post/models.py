from django.db import models
class Post(models.Model):
    title = models.CharField(        
        max_length=150,
        default="",
        blank=True,
        null=True,
        )
    content= models.TextField(
        max_length=500,
        default="",
        blank=True,
        null=True,
    )
    like = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    post= models.ForeignKey(Post,on_delete=models.CASCADE)
    content=models.TextField(
        max_length=500,
        default="",
        blank=True,
        null=True,
    )
    createAt= models.DateField(auto_now_add=True)
    updateAt=models.DateField(auto_now=True)
    
