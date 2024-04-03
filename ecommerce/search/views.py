from django.shortcuts import render
from shop.models import product,category
from django.db.models import Q
# Create your views here.

def searchproducts (request):
    """ search product code """
    p=None
    query=""
    if(request.method=="POST"):
        query = request.POST['q']
        # print(query)
        if(query):
            p=product.objects.filter(Q(name__icontains=query) | Q(desc__icontains=query))
            # i=category.objects.filter(Q(name__icontains=query) | Q(desc__icontains=query))
            """ we can use iconatains or contains contains take only the lower letters icontains all the letters """
            """ Q we have to use Q when we use logical and or not gate """
            # print(p)
    return render(request,'search.html',{'p':p,'q':query})


