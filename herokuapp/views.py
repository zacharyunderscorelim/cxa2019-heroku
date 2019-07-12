from django.shortcuts import render
from herokuapp.forms import CategoryForm
from herokuapp.models import Category, Page, UserProfile
from herokuapp.forms import UserForm,  PageForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views import generic




def about(request):
    # The context contains information such as the client's machine details, for
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.


    return render(request, 'about.html')








def about_fbsg(request):
    # The context contains information such as the client's machine details, for
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'about_fbsg.html')


def decode_url(url):
    return url.replace('_', ' ')

def encode_url(url):
    return url.replace(' ', '_')

def index(request):
    category_list = Category.objects.order_by('name')[:20]
    context_dict = {'categories':category_list}
    for category in category_list:
        category.url = category.name.replace(' ', '_')
    return render(request, 'index.html', context_dict)

def category(request, category_name_url):
    # Change underscores in the category name to spaces.
    # URLs don't handle spaces well, so we encode them as underscores.
    # We can then simply replace the underscores with spaces again to get the name.
    category_name = category_name_url.replace('_', ' ')
    # Create a context dictionary which we can pass to the template rendering engine. # We start by containing the name of the category passed by the user.
    context_dict = {'category_name': category_name, 'category_name_url': category_name_url}
    try:
        # Can we ﬁnd a category with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        category = Category.objects.get(name=category_name)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category

    except Category.DoesNotExist:
        pass

    return render(request,'category.html', context_dict)

@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)
    else:
        form = CategoryForm()
        return render(request, 'add_category.html', {'form': form})

@login_required
def add_page(request, category_name_url):
    category_name = decode_url(category_name_url)
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
    # This time we cannot commit straight away. # Not all ﬁelds are automatically populated!
            page = form.save(commit=False)
    # Retrieve the associated Category object so we can add it.
            cat = Category.objects.get(name=category_name)
            page.category = cat
            page.views = 0
            page.save()
    # With this, we can then save our new model instance.

    # Now that the page is saved, display the category instead.
            return category(request, category_name_url)
        else:
            print(form.errors)
    else:
        form = PageForm()
    return render(request, 'add_page.html', {'category_name_url': category_name_url, 'category_name': category_name, 'form': form})



def register(request):
    #boolean value
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()


            registered = True

        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request, 'register.html',
    {'user_form': user_form, 'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/herokuapp/')
            else:
                return HttpResponse("Your herokuapp account has been hacked.")
        else:
            print("Messed up login details:{0},{1}".format(username,password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'login.html', {})


@login_required
def restricted(request):
    return HttpResponse("Since you're in, you can see this text")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/herokuapp/')



