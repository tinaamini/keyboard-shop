from django import forms


class CartAddForm(forms.Form):
    quality=forms.IntegerField(min_value=1,max_value=9,initial=1)
    color=forms.CharField()