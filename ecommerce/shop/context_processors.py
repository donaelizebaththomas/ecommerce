

from shop.models import category

# the data we are taking we can use in any html file


def links(request):
    c=category.objects.all()
    return{'links':c}