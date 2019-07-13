from herokuapp.models import Page, Category, Shop
from herokuapp.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.gis import forms

FOOD_CHOICES = (
    ('carbs','Carbohydrates'),
    ('meat', 'Meat'),
    ('veg','Vegetables'),
    ('dairy','Dairy'),
    ('others','Others'),
)

URGENCY = (
    ('fuck', 'Ultra Urgent'),
    ('shit', 'Urgent'),
    ('norm', 'Normal'),
    ('meh', 'Not too urgent'),
)

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the type of food!")

    class Meta:
    # Provide an association between the ModelForm and a model
        model = Category
        fields = ('name',)


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the name of the food")
    url = forms.ChoiceField(choices=FOOD_CHOICES, help_text="Please select the type of food it is")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)




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

class ShopForm(forms.ModelForm):
    name = forms.CharField(max_length=100, help_text="Please enter your Company name")
    location = forms.PointField(help_text="Please pin your company's location on the map")
    address = forms.CharField(max_length=150, help_text="Please enter your company's address")
    city = forms.CharField(max_length=50, help_text="Please input your City")
    urge = forms.ChoiceField(choices=URGENCY, help_text="Please state how urgent the food is!")
    
    class Meta:
        model = Shop
        fields = ('name','location','address','city','urge')
    

