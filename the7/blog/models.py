from django.db import models

class Post(models.Model):
    post_name = models.CharField(max_length=255)
    post_image = models.ImageField()
    post_date = models.DateTimeField(auto_now=True)
    post_type = models.CharField(max_length=255)
    post_content = models.TextField()

    def __str__(self):
        return self.post_name
