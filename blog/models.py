from django.db import models

# Create your models here.

class Blog(models.Model):
    blog_title = models.CharField(max_length=200, blank=False, null=False)
    blog_text = models.TextField(max_length=1000, blank=False, null=False)
    blog_Img = models.ImageField(upload_to="image")
    blog_date = models.DateField(auto_now_add=True)
    BlogUpdate_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.blog_title
    



