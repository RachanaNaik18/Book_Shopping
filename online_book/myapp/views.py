from django.shortcuts import render, HttpResponseRedirect
from .models import book,Cart,Address,Order
from .forms import book_form, Signup_form
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout

# Create your views here.
# def Home(request):
#     a = book.objects.all()
#     return render(request, 'index.html', {'data':a})

def find(request):
    if request.method == "POST":
        search = request.POST.get('search')
        all = book.objects.all()
        os = book.objects.filter(Q(Name__icontains = search) | Q(Author__icontains=search) | Q(Publisher__icontains=search) | Q(category__icontains=search))
        print(os)

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
        if request.method == "POST":
            search = request.POST.get('search')
            # all = book.objects.all()
            a = book.objects.filter(Q(Name__icontains = search) | Q(Author__icontains=search) | Q(Publisher__icontains=search) | Q(category__icontains=search))
        else:
            a = book.objects.all()
            cart1 = Cart.objects.filter(user=request.user)
            coun = cart1.count()
            uname = request.user
            b = Address.objects.all().values_list('id', flat=True)
            return render(request, 'cart.html', {'data':a, 'cartcount':coun, 'uname':uname})
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
        return render(request, 'showcart.html', {'data':cart1,'quantity':qua, 'uname':uname})
    else:
        return HttpResponseRedirect('/login/')
    
def Remove_cart(request, id):
    if request.method == "GET":
        os = Cart.objects.filter(website_id = id)
        os.delete()
        return HttpResponseRedirect('/viewcart/')
    
def cart_increase(request):
    if request.method == "GET":
        cid = request.GET.get('cid')
        items, store = Cart.objects.get_or_create(website_id = cid)

        if not store:
            items.quantity += 1
            items.save()
        
        return HttpResponseRedirect('/viewcart/')

def cart_decrease(request):
    if request.method == "GET":
        cid = request.GET.get('cid')
        items,store = Cart.objects.get_or_create(website_id = cid)

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
    if request.user_is_authenticated:
        if request.method == "POST":
            product_id = request.POST.get('pid')
            cart_id = request.POST.get('cid')

            Order.objects.create(user = request.user)
        

def address_user(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            city = request.POST.get('city')
            pincode = request.POST.get('pincode')
            city = request.POST.get('city')
