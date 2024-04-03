
from cart.models import Cart

def total(request):
    if request.user.is_authenticated:
        user_cart = Cart.objects.filter(user=request.user)
        total_quantity = sum(cart_item.quantity for cart_item in user_cart)
        return {'Total': total_quantity}
    else:
        # You might want to handle the case where the user is not authenticated.
        # You can return a total of 0 or handle it differently based on your requirement.
        return {'Total': 0}

# from cart.models import Cart
#
# # to take the count of the total number of product in the cart
#
#
# def total(request):
#      if request.user.is_authenticated:
#         u=request.user
#         c=Cart.objects.filter(user=u)
#         total =0
#         try:
#             for i in c:
#                 total = total + i.quantity
#         except:
#             total=0
#
#         return{'Total':total}