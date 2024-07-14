from math import e
from django.shortcuts import render,HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout

from Main.models import Book,Cart

# Create your views here.


def mainScreen(request):
    emps = Book.objects.all()
    context = {
        'emps': emps
    }
    return render(request,'Home.html',context)


def signup(request):
    return render(request, 'signup.html')


def profile(request):
    return render(request, 'profile.html')


def settings(request):
    return render(request, 'settings.html')


def about_us(request):
    return render(request, 'about_us.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print(username, password)
            return redirect(mainScreen)
        else:
            messages.info(request, "Invalid username or password")
            return redirect(login)
    return render(request, 'login.html')


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        print(username, email, password)
        if User.objects.filter(username=username).exists():
            messages.info(
                request, "Username already exists. Try with different username.")
            return redirect(signup)
        else:
            user = User.objects.create_user(
                username=username, email=email, password=password)
            user.set_password(password)
            user.save()
            if user is not None:
                auth.login(request, user)
                print(username, password)
                return redirect(mainScreen)
            else:
                return redirect(signup)
    else:
        return render(request, 'signup.html')


def logout(request):
    auth_logout(request)
    return redirect(mainScreen)

def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        authors = request.POST['authors']
        publisher = request.POST['publisher']
        published_date = request.POST['published_date']
        description = request.POST['description']
        isbn_13 = request.POST['isbn_13']
        page_count = request.POST['page_count']
        thumbnail_url = request.POST['thumbnail_url']
        # booked = False
        available = int(request.POST['available'])
        new_book = Book(title=title, authors=authors, publisher=publisher, published_date=published_date, description=description, isbn_13=isbn_13, page_count=page_count, thumbnail_url=thumbnail_url,available = available)
        
        
        new_book.save()
        return HttpResponse('Book added Successfully')
    elif request.method=='GET':
        return render(request, 'add_book.html')
    else:
        return HttpResponse("An Exception Occured! Employee Has Not Been Added")

    
def remove_book(request):
    if request.method == 'POST':
        isbn_13 = request.POST.get('isbn_13')
        book_to_be_removed = get_object_or_404(Book, isbn_13=isbn_13)
        book_to_be_removed.delete()
        return HttpResponse("Book Removed Successfully")
    
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'remove_book.html', context)

def confirm_remove_book(request, isbn_13):
    book_to_remove = get_object_or_404(Book, isbn_13=isbn_13)
    context = {
        'book_to_remove': book_to_remove
    }
    return render(request, 'confirm_remove_book.html', context)

@login_required
def add_to_cart(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, book=book)
    if created:
        cart_item.save()
    return redirect('view_cart')

@login_required
def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    return render(request, 'view_cart.html', {'cart_items': cart_items})