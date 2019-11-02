from django.forms import ModelForm
from content.models import Article

class ArticleModelForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title','content','active']