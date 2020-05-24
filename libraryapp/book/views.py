from django.shortcuts import render,redirect
from .models import Book
from .forms import Bookcreate
from django.http import HttpResponse

# Create your views here.
def index(request):
    shelf= Book.objects.all()
    return render(request,'book/index.html',{'shelf':shelf})


def upload(request):
    upload=Bookcreate()
    if request.method== 'POST':
        upload=Bookcreate(request.POST,request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is invalid""",'index')
    
    else:
        return render(request,'book/upload.html',{'upload':upload})



def update_book(request,book_id):
    book_id=int(book_id)
    try:
        book_sel=Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return redirect('index')
    Book_form=Bookcreate(request.POST or None,instance=book_sel)
    if Book_form.is_valid():
        Book_form.save()
        return redirect('index')
    return render(request,'book/upload.html',{'upload':Book_form})


def delete_book(request,book_id):
    book_id=int(book_id)
    try:
        book_sel=Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return redirect('index')
    book_sel.delete()
    return redirect('index')









