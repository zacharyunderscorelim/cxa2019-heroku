from django import forms
from herokuapp.models import Page, Category
from herokuapp.models import UserProfile
from django.contrib.auth.models import User



class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the food type.")

    class Meta:
    # Provide an association between the ModelForm and a model
        model = Category
        fields = "__all__"


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        # If url is not empty and doesn't start with 'http://', prepend 'http://'.
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url
        return cleaned_data
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Page
        # What ﬁelds do we want to include in our form?
        # This way we don't need every ﬁeld in the model present.
        # Some ﬁelds may allow NULL values, so we may not want to include them… # Here, we are hiding the foreign key.
        fields = ('title', 'url', 'views')

class UserForm(forms.ModelForm):
    username = forms.CharField(help_text="Please enter a username.")
    email = forms.CharField(help_text="Please enter your email.")
    password = forms.CharField(widget=forms.PasswordInput(), help_text="Please enter a password.")
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    website = forms.URLField(help_text="Please enter your website.", required=False)
    picture = forms.ImageField(help_text="Select a proﬁle image to upload.",required=False)
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')


