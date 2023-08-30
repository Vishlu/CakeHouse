from django.shortcuts import render
from .forms import Order
from .models import Userinformation
from django.contrib import messages

# Create your views here.
def order(request):
    if request.method == 'POST':
        form = Order(request.POST)
        if form.is_valid():
            un = form.cleaned_data['user_name']
            fm = form.cleaned_data['first_name']
            ln = form.cleaned_data['last_name']
            em = form.cleaned_data['email_id']
            ph = form.cleaned_data['phone_no']
            add = form.cleaned_data['address']
            loc = form.cleaned_data['location']
            ck = form.cleaned_data['cake']
            qn = form.cleaned_data['quantity']
            ui = Userinformation(user_name=un, first_name=fm, last_name=ln, email_id=em, phone_no=ph, address=add, location=loc, cake=ck, quantity=qn)
            ui.save()
            messages.success(request,'Hey Guy !, Your Order are Submited.')
            form = Order()
    
    else:        
        form = Order()
    return render(request, 'order/order.html', {'order':form})