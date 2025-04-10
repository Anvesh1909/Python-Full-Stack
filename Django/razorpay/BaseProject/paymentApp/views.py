from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Transaction
from .forms import PaymentForm
from django.conf import settings
import razorpay

def initiate_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            amount_rupees = form.cleaned_data['amount']
            amount_paise = amount_rupees * 100

            client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

            payment = client.order.create({
                'amount': amount_paise,
                'currency': 'INR',
                'payment_capture': '1'
            })

            transaction = Transaction.objects.create(
                name=name,
                email=email,
                amount=amount_rupees,
                order_id=payment['id']
            )

            context = {
                'payment': payment,
                'transaction': transaction,
                'razorpay_key_id': settings.RAZORPAY_KEY_ID,
                'amount': amount_paise,
                'amount_rupees': amount_rupees,
                'name': name,
                'email': email,
            }
            return render(request, 'payment_page.html', context)
    else:
        form = PaymentForm()
    return render(request, 'initiate_payment.html', {'form': form})



@csrf_exempt
def verify_payment(request):
    if request.method == "POST":
        data = request.POST
        try:
            client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
            client.utility.verify_payment_signature({
                'razorpay_order_id': data['razorpay_order_id'],
                'razorpay_payment_id': data['razorpay_payment_id'],
                'razorpay_signature': data['razorpay_signature']
            })

            transaction = Transaction.objects.get(order_id=data['razorpay_order_id'])
            transaction.payment_id = data['razorpay_payment_id']
            transaction.signature = data['razorpay_signature']
            transaction.is_verified = True
            transaction.save()

            return render(request, 'payment_success.html', {'transaction': transaction})
        except:
            return render(request, 'payment_failed.html')



def transaction_list(request):
    transactions = Transaction.objects.filter(is_verified=True).order_by('-created_at')
    return render(request, 'transaction_list.html', {'transactions': transactions})
