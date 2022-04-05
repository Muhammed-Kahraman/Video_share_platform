# Import
from django.db import models
from videos.validators import validate_file_extension


# Create your models here.
class Video(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=50, editable=True)
    video_file = models.FileField(upload_to='media/',null=True, verbose_name="Video (Only .mp4)", validators=[validate_file_extension], editable=True)
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title + ": " + str(self.video_file).replace("videos/", "").replace(".mp4", "")

    class Meta:
        ordering = ['-created_date']


class Comments(models.Model):
    article = models.ForeignKey(Video, on_delete=models.CASCADE, verbose_name="Article", related_name="comments")
    comment_author = models.CharField(max_length=50,verbose_name="Name:")
    comment_content = models.CharField(max_length=250, verbose_name="Comment")
    created_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-created_date']
