from django.http import HttpResponse
from bookapp.models import BookModel
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserCreationForm, LoginForm


# Create your views here.
def books_list_view(request):
    books = BookModel.objects.all()
    q = request.GET.get('q')
    if q:
        books = books.filter(name__icontains=q)

    context = {'books': books}
    return render(request, 'books.html', context)


def book_detail_view(request, pk):
    book = BookModel.objects.filter(id=pk).first()
    if book:
        context = {'book': book}
        return render(request, 'book-detail.html', context)
    else:
        return HttpResponse('Book not found')


def download_detail_view(request, pk):
    book = BookModel.objects.filter(id=pk).first()

    if book:
        file_path = str(book.ebooks)
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/pdf')
            return response
    else:
        return HttpResponse('Book not found')


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('books:list')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books:login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
