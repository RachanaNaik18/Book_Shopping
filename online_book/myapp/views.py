from django.shortcuts import render, HttpResponseRedirect
from .models import book,Cart,Address,Order, Delivered
from .forms import book_form, Signup_form
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from razorpay import Client
import datetime



def find(request):
    if request.method == "POST":
        search = request.POST.get('search')
        all = book.objects.all()
        os = book.objects.filter(Q(Name__icontains = search) | Q(Author__icontains=search) | Q(Publisher__icontains=search) | Q(category__icontains=search))
        

    else:
        os = book.objects.all()
    return render(request, 'index.html', {'data':os})

def  data(request):
    if request.method == "POST":
        fm = book_form(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Data Added Successfully...")
            return HttpResponseRedirect("/home/")
    
    else:
        fm = book_form()
    return render(request, 'data_entry.html', {'form':fm})

def update(request, id):
    if request.method == "POST":
        pi = book.objects.get(pk = id)
        fm = book_form(request.POST, instance=pi)

        if fm.is_valid():
            fm.save()
            messages.success(request, "Data Updated Successfully...")

    else:
        pi = book.objects.get(pk = id)
        fm = book_form(request.POST, instance=pi)
    return render(request, "update.html", {'form1':fm})

def delete(request, id):
    if request.method == "POST":
        pi = book.objects.get(pk = id)
        pi.delete()
        messages.success(request, "Data Deleted Successfully...")
        return HttpResponseRedirect("home/")
    
def Cart_search(request):
    if request.user.is_authenticated:
        cart1 = Cart.objects.filter(user=request.user)
        count = cart1.count()
        uname = request.user

        j_img = book.objects.filter(category__iexact="Journal").order_by('-id')[:3]
        n_img = book.objects.filter(category__iexact="Novel").order_by('-id')[:3]
        c_img = book.objects.filter(category__iexact="Comics").order_by('-id')[:3]

        if request.method == "POST":
            search = request.POST.get('search')
            a = book.objects.filter(Q(Name__icontains = search) | Q(Author__icontains=search) | Q(Publisher__icontains=search) | Q(category__icontains=search))
     
        else:
            a = book.objects.all()
        return render(request, 'cart.html', {'data':a, 'cartcount':count, 'uname':uname, 'j_img':j_img, 'n_img':n_img, 'c_img':c_img})
    else:
        return HttpResponseRedirect('/login/')

def add_to_cart(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            cid = request.GET.get('cid')
            items,store = Cart.objects.get_or_create(website_id = cid, user=request.user)
            if not store:
                items.quantity +=1
                items.save()

            return HttpResponseRedirect('/cart/')

def view_cart(request):
    if request.user.is_authenticated:
        user_cart = Cart.objects.filter(user=request.user).values_list('website_id', flat = True)
        cart1 = book.objects.filter(id__in = user_cart)
        qua= Cart.objects.filter(user=request.user)
        uname = request.user

        cart2 = Cart.objects.filter(user=request.user)
        count = cart2.count()

        amount = book.objects.filter(id__in = user_cart).values_list('Price', flat=True)
        number_books = Cart.objects.filter(user=request.user).values_list('quantity', flat = True)
        mul_amt_book = []
        for i in range (0, len(amount)):
            mul_amt_book.append(amount[i]*number_books[i])
        add_amount = sum(mul_amt_book)

        
        a = Cart.objects.filter(user=request.user).values_list('quantity', flat=True)
        total = 0
        for i in range(0, len(a)):
            total = total + a[i]
        return render(request, 'showcart.html', {'data':cart1,'quantity':qua, 'uname':uname, 'total_items':total, 'add_amt': add_amount, 'cartcount':count})
    else:
        return HttpResponseRedirect('/login/')
    
def Remove_cart(request, id):
    if request.method == "GET":
        os = Cart.objects.filter(website_id = id)
        print(os)
        os.delete()
        return HttpResponseRedirect('/viewcart/')
    
def cart_increase(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            cid = request.GET.get('cid')
            items, store = Cart.objects.get_or_create(website_id = cid, user=request.user)
            print(items)

            if not store:
                items.quantity += 1
                items.save()
            return HttpResponseRedirect('/viewcart/')

def cart_decrease(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            cid = request.GET.get('cid')
            items,store = Cart.objects.get_or_create(website_id = cid,user=request.user)     

            if not store:
                items.quantity -= 1
                items.save()
                if items.quantity < 1:
                    items.delete()

            return HttpResponseRedirect('/viewcart/')

def Signup(request):
    if request.method == "POST":
        fm = Signup_form(request.POST)
        if fm.is_valid():
            fm.save()
            fm = Signup_form()
    else:
        fm = Signup_form()

    return render(request, "signup.html", {'form': fm}) 

def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user  = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/cart/')
        
    return render(request, 'login.html')

def LogOut(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def Order_place(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            product_id = request.POST.get('pid')
            Order.objects.create(user = request.user, Buy_direct_id=product_id)
            return HttpResponseRedirect('/address/')
        
def Order_place1(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            cart_id = Cart.objects.filter(user=request.user).values_list('website_id', flat=True)
            cart_id1 = Cart.objects.filter(user=request.user).values_list('id', flat=True)
            quantity = Cart.objects.filter(user=request.user).values_list('quantity', flat=True)
   
            p_id = book.objects.filter(id__in=cart_id).values_list('id',flat=True)
            for i in range(0, len(p_id)):
                # print(cart_id1[i], p_id[i])
                Order.objects.create(user = request.user, Buy_direct_id = p_id[i], Buy_cart_id = cart_id1[i], quantity = quantity[i])  
            return HttpResponseRedirect('/address/')
    
def address_user(request):
    if request.user.is_authenticated:

        client = Client(auth=('rzp_test_r1SMDlPAi7bpbD','WIaNqW59qPAI8Em361bFxCVh'))
        amount=500
        data = { "amount": amount, "currency": "INR", "receipt": "order_rcptid_11" }
        client.order.create(data=data)
        
        quantity = Cart.objects.filter(user=request.user)

        order = Order.objects.filter(user=request.user).values_list('Buy_direct_id', flat=True)
        data1 = book.objects.filter(id__in=order) 

        user_ord = Order.objects.filter(user=request.user).values_list('Buy_direct_id', flat = True)
        amount = book.objects.filter(id__in = user_ord).values_list('Price', flat=True)
        number_books = Order.objects.filter(user=request.user).values_list('quantity', flat = True)
        mul_amt_book = []
        for i in range (0, len(amount)):
            mul_amt_book.append(amount[i]*number_books[i])
        add_amount = sum(mul_amt_book)
        a = Order.objects.filter(user=request.user).values_list('quantity', flat=True)
        total = 0
        for i in range(0, len(a)):
            total = total + a[i]
        print(total)
        
        if request.method == "POST":
            street=request.POST.get('street')
            city = request.POST.get('city')
            pincode = request.POST.get('pincode')
            state = request.POST.get('state')
            product_id = request.POST.get('pid')
            Address.objects.create(street=street,City=city, Pincode=pincode, State = state, user=request.user, product_id=product_id)

        os = Address.objects.filter(user_id = request.user)    
        return render(request, 'add.html', {'user_add':os, 'data':data1, 'quantity':quantity, 'q':total, 't_amt':add_amount})
    else:
        return HttpResponseRedirect('/login/')

def go_back(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            g_cart = Order.objects.all()
            g_cart.delete()
            return HttpResponseRedirect('/cart/')

def remove_add(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            ct = request.GET.get('add_id')
            os = Address.objects.filter(id__in = ct)
            os.delete()
            return HttpResponseRedirect('/address/')

def Delivary(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            order = Order.objects.filter(user=request.user).values_list('Buy_direct_id', flat=True)
            data = book.objects.filter(id__in=order).values_list('id', flat=True)
            ord_no = Order.objects.filter(user=request.user).values_list('order_id', flat=True)
            qu = Cart.objects.filter(user=request.user).values_list('quantity', flat=True)
            c = Order.objects.filter(user=request.user).values_list('id', flat=True)

            
            
            for i in range(0, len(data)):
                d = datetime.datetime.now() + datetime.timedelta(days=5)
                Delivered.objects.create(book_Cart_id=data[i] ,user=request.user, order_id_no=ord_no[i], quantity= qu[i], date=d)
                
                if ord_no[i] in ord_no:
                    pi = Order.objects.filter(id__in = c)
                    pi.delete()
        return HttpResponseRedirect('/del_pla/')
    
def cart_del(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            c_t = Order.objects.filter(user=request.user).values_list('Buy_cart_id', flat=True)
            cart = Cart.objects.filter(id__in=c_t)
            cart.delete()
        return HttpResponseRedirect('/address/')

def Delivary_placed(request):
    if request.user.is_authenticated:
        d= Delivered.objects.filter(user=request.user).values_list('book_Cart_id', flat=True)
        data=book.objects.filter(id__in=d)
        
        k = Delivered.objects.filter(user=request.user)

        uname = request.user

        cart1 = Cart.objects.filter(user=request.user)
        count = cart1.count()

        amount = book.objects.filter(id__in = d).values_list('Price', flat=True)
        num_books = Delivered.objects.filter(user=request.user).values_list('quantity', flat = True)
        
        mul_amt_book = []
        for i in range (0, len(amount)):
            mul_amt_book.append(amount[i]*num_books[i])
        
        return render(request, "delivered.html", {'data':data, 'deli':k, 'uname':uname, 'amt':mul_amt_book, 'cartcount':count})

def confirm(request):
    return render(request,'confirm.html')