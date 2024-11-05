from django.urls import path
from .views import cart_page, checkout_home, cart_update, checkout_done_view, cart_get_items

app_name = "carts"

urlpatterns = [
    path('', cart_page, name='home'),
    path('checkout/success/', checkout_done_view, name='success'),
    path('checkout/', checkout_home, name='checkout'),
    path('update/', cart_update, name='update'),
    path('get-items/', cart_get_items, name='cart-get-items'),
]