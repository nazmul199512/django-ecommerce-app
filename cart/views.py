from django.shortcuts import render
from .models import Cart


def cart(request):

     cart_id = request.session.get('cart_id', None)
     if cart_id is None:

          cart_obj = Cart.objects.create(user=None)
          request.session['cart_id'] = cart_obj.id
          print('New cart created')
     else:
          print('cart Id exist')
          print(cart_id)
          cart_obj = Cart.objects.get(id=cart_id)

     return render(request, 'cart/cart.html', {})
