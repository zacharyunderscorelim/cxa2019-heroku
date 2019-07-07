import os

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title, url=url, views=views)[0]
    return p
def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    return c

def presets_url():
    python_cat = add_cat('Blah')
    add_page(cat=python_cat, title="Ofﬁcial Python Tutorial", url="https://www.google.com")
    add_page(cat=python_cat, title="Learn Python in 10 Minutes", url="https://www.google.com")

    django_cat = add_cat("Blahs")
    add_page(cat=django_cat, title="Ofﬁcial Django Tutorial", url="https://www.google.com")
    add_page(cat=django_cat, title="Django Rocks", url="https://www.google.com")

    frame_cat = add_cat("Baa")
    add_page(cat=frame_cat, title="Bottle", url="https://www.google.com")
    add_page(cat=frame_cat, title="Flask", url="https://www.google.com")

# Print out what we have added to the user. for c in Category.objects.all():
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("-",str(c),"-",str(p))


if __name__== '__main__':
    print("Starting helloApp population script")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoherokuapp.settings')
    import django
    django.setup()
    from herokuapp.models import Category, Page
    presets_url()
