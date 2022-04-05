from django.forms import ModelForm

from videos.models import Video

class ArticleForm(ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'video_file']
