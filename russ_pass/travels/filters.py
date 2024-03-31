from django_filters import FilterSet, ModelChoiceFilter
from .models import Replies, Ads
 

class ReplyFilter(FilterSet):

    class Meta:
        model = Replies
        fields = {'ad': ['exact'],
        } 
