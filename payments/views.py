import stripe
from django.shortcuts import render,redirect
from django.conf import settings
from payments.models import Item
from django.http import JsonResponse, HttpResponse
from pprint import pprint


stripe.api_key = settings.STRIPE_API_KEY


def api_item(request, pk):
    try:
        item = Item.objects.get(id=pk)        
    except Item.DoesNotExist:
        return JsonResponse(
            {'error': f'Item with id={pk} not found'},
            json_dumps_params={
                'ensure_ascii': False,
                'indent': 4,
            }
        )
    
    context = {
        'item': item
    }
    
    return render(request, 'buy_item.html', context)


def api_buy(request, pk):
    try:
        item = Item.objects.get(id=pk)        
    except Item.DoesNotExist:
        return redirect('cancel')   
    
    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                'name': item.name,
                },
                'unit_amount': int(item.price * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=f'http://{settings.PAYMENT_REDIRECT}/success',
        cancel_url=f'http://{settings.PAYMENT_REDIRECT}/cancel',
    )

    return redirect(session.url, code=303)


def success(request):
       
    return HttpResponse('<html><body><h1>Thanks for your order!</h1></body></html>')


def cancel(request):
    
    return HttpResponse('<html><body><h1>Something went wrong..</h1></body></html>')

