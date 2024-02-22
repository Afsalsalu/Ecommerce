from django.shortcuts import render
from.models import Product, Contact, TopRanking
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from .models import Checkout
from django.shortcuts import render, get_object_or_404



#Stripe import
import stripe
from django.conf import settings
from django.views import View
from django.contrib import messages


# Create your views here.

def index(request):
    context={
        'produ':Product.objects.all(),
        'Tr':TopRanking.objects.all()
    }
    return render(request,'web/index.html',context)
    

def login1(request):
    if request.method=="POST":
        username=request.POST.get('email')
        password=request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return redirect('register')
        


    return render(request,'web/login.html')

def register(request):

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2:
            messages.warning(request, 'Passwords do not match')
        else:
            if User.objects.filter(username=username).exists():
                messages.warning(request, 'Username already exists')
            else:
                new_user = User.objects.create_user(username, email, password)
                new_user.first_name = username
                new_user.save()
                return redirect('login')
    



    return render(request,'web/register.html')

def home2(request):
    return render(request,'web/home-2.html')

def home3(request):
    return render(request,'web/home-3.html')


def contact(request):
    if request.method == "POST":
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        message=request.POST.get('message')

        contact1=Contact(
            firstname=firstname,
            lastname=lastname,
            email=email,
            message=message
    
        )
        contact1.save()

    return render(request,'web/contact.html')

def cart(request):
    return render(request, 'web/shopping-cart.html')


def logout1(request):
    logout(request)
    return redirect('index')






@login_required(login_url="login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")


@login_required(login_url="login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart")


@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart")


@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart")


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart")


@login_required(login_url="login")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')




def checkout(request):

    
    return render(request,'web/checkout.html')


def placeorder(request):
    if request.method == "POST":
        fname=request.POST.get('first_name')
        lname=request.POST.get('last_name')
        company=request.POST.get('company')
        country=request.POST.get('country')
        address=request.POST.get('address')
        
        pincode=request.POST.get('pincode')
        phone=request.POST.get('phone')
        email=request.POST.get('email')

        checkout1=Checkout(
            first_name=fname,
            last_name=lname,
            company=company,
            country=country,
            address=address,
            
            pincode=pincode,
            phone=phone,
            email=email
         )
        checkout1.save()

        # for i in cart:
        #     a = float(cart[i]['price'])
        #     b=int(cart[i]['quantity'])
        #     total=a*b

        #     order2=OrderItems(
        #         order=checkout1,
        #         Product=cart[i]['name'],
        #         image=cart[i]['image'],
        #         price=cart[i]['price'],
        #         quantity=cart[i]['quantity'],
        #         total=total
        #     )
        #     order2.save()
            

    return render(request, 'web/placeorder.html')


def error_404_view(request, exception):
    return render(request, 'web/404.html')

stripe.api_key = settings.STRIPE_SECRET_KEY

class CreateStripeCheckoutSessionView(View):
    """
    Create a checkout session and redirect the user to Stripe's checkout page
    """

    def post(self, request, *args, **kwargs):
        price1 = Product.objects.all()
        for p in price1:
            price2=  p.price
            name1 = p.name

        
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "unit_amount": int(price2),
                        "product_data": {
                            "name": name1,
                            
                                
                        },
                    },
                    "quantity":1,
                }
            ],
            mode="payment",
            success_url='http://localhost:8000/seccess',
            cancel_url='http://localhost:8000/placeorder',
        )
        return redirect(checkout_session.url)


def sccessfull(request):
    return render(request,'web/seccess.html')




def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'web/detail.html', {'product': product})



def wishlist(request):
    return render(request, 'web/wishlist.html')