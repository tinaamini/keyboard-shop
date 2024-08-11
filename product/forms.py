from django import forms
from .models import Attributes
class SearchForm(forms.Form):
    query = forms.CharField(label='جستجو', max_length=100)




class ColorFilterForm(forms.Form):
    color = forms.ChoiceField(required=False, choices=[('', 'تمام رنگ‌ها')], label='رنگ')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        colors = Attributes.objects.filter(type='color').values_list('title', flat=True).distinct()
        self.fields['color'].choices += [(color, color) for color in colors]