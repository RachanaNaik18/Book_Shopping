from django.shortcuts import render, HttpResponseRedirect
from .models import book,Cart
from .forms import book_form
from django.contrib import messages
from django.db.models import Q

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
    if request.method == "POST":
        search = request.POST.get('search')
        all = book.objects.all()
        a = book.objects.filter(Q(Name__icontains = search) | Q(Author__icontains=search) | Q(Publisher__icontains=search) | Q(category__icontains=search))
        print(a)
    else:
        a = book.objects.all()
    return render(request, 'cart.html', {'data':a})
# def Cart(request):
#     a = book.objects.all()
#     print(a)
#     return render(request, 'cart.html', {'data':a})

def add_to_cart(request):
    if request.method == "GET":
        cid = request.GET.get('cid')
        store = Cart.objects.create(website_id = cid)
        store.save()
        return HttpResponseRedirect('cart/')

def view_cart(request):
    user_cart = Cart.objects.all().values_list('website_id', flat = True)
    return render(request, 'showcart.html')

