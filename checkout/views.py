from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OrmtT05x7uMoVaU6pmqC4XdMUDxZo11wphgG6jlNxwZpt3u4CATvqF0EXtiFyxPsixYPC3Uq8n4doG8BT7MLvHR00Tb1m2HwP',
        'client_secret': 'sk_test_51OrmtT05x7uMoVaUHRgaZgfs7WYtGk7epDk8KyW4F8uqG7mM6SFMW1hPKXhYgNCaFDiTgu9w16Yq8jARC8M1R2oI00dhonEKaD',
    }

    return render(request, template, context)