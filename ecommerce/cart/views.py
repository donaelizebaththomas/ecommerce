from django.shortcuts import render
from shop.models import product
from cart.models import Cart,Order,Account
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required      # it requires login to add things to the cart
def cart_view(request):
    """ for displaying cart """
    u=request.user
    c=Cart.objects.filter(user=u)
    total=0
    for i in c:
        total=total+i.quantity*i.Product.price
    return render(request,'cart.html',{'c':c,'total':total})


@login_required      # it requires login to add things to the cart
def addtocart(request,p):
    """ to add the element to the cart """
    p=product.objects.get(id=p)
    u=request.user # to get the details of the current user
    try:
        # if there is already the same product it will increase the quantity of the product
        cart=Cart.objects.get(user=u,Product=p)
        if(p.stock>0):
            cart.quantity+=1
            p.stock -= 1
            p.save()
            cart.save()

    except:
        # if there is no product then it will create a product
        if (p.stock > 0):
            cart=Cart.objects.create(Product=p,user=u,quantity=1)
            p.stock -= 1
            cart.save()

    return cart_view(request)

def cart_remove(request,p):
    """ to decrease the element in the cart """
    p = product.objects.get(id=p)
    u = request.user  # to get the details of the current user
    try:
        # if there is already the same product it will increase the quantity of the product
        cart = Cart.objects.get(user=u, Product=p)
        if (cart.quantity > 1):
            cart.quantity -= 1
            cart.save()
            p.stock += 1
            cart.save()
        else:
            cart.delete()
            p.stock +=1
            p.save()

    except:
        pass

    return cart_view(request)

def full_remove(request,p):
    """ to delete the element from the cart"""
    p = product.objects.get(id=p)
    u = request.user  # to get the details of the current user
    try:
        # if there is already the same product it will increase the quantity of the product
        cart = Cart.objects.get(user=u, Product=p)
        cart.delete()
        p.stock +=  cart.quantity
        p.save()
    except:
        pass
    return cart_view(request)


def orderform(request):
    if request.method == "POST":
        a = request.POST['a']
        n = request.POST['n']
        an = request.POST['an']

        u = request.user
        c = Cart.objects.filter(user=u)

        total = 0
        for item in c:
            total += item.quantity * item.Product.price

        try:
            ac = Account.objects.get(acctnum=an)
            if ac.amount >= total:
                ac.amount -= total
                ac.save()
                for item in c:
                    order = Order.objects.create(
                        user=u,
                        Product=item.Product,  # Assign product directly from cart item
                        address=a,
                        phone=n,
                        no_of_item=item.quantity,
                        order_status="paid"
                    )
                    order.save()

                c.delete()
                msg = "Order Placed successfully"
                return render(request, 'orderdetails.html', {'message': msg})
            else:
                msg = "Insufficient funds"
                return render(request, 'orderdetails.html', {'message': msg})
        except Account.DoesNotExist:
            msg = "Account does not exist"
            return render(request, 'orderdetails.html', {'message': msg})

    return render(request, 'Orderform.html')

def orderview(request):
    u=request.user
    o=Order.objects.filter(user=u)
    return render(request,'orderview.html',{'o':o,'u':u})
