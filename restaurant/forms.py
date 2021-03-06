from django import forms

from .models import Restaurant, FoodItem


class LoginForm(forms.Form):
    username = forms.CharField(label="Username",
                                widget=forms.TextInput(
                                        attrs={'placeholder': 'Username'}))
    password = forms.CharField(label="Password",
                                widget=forms.PasswordInput(
                                        attrs={'placeholder': 'Password'}))

class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        exclude = ['restaurant', 'times_ordered']

class RestaurantProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(RestaurantProfileForm, self).__init__(*args, **kwargs)
        self.fields["address_emirate"].widget.attrs['style'] = 'display: block'

    class Meta:
        model = Restaurant
        exclude = ['user']
