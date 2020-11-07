from django.shortcuts import render,redirect
from Books.models import Book
from Books.forms import BookCreateForm,BookupdateForm

# Create your views here.
def bookcreate(request):
    template_name="create.html"
    form=BookCreateForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=BookCreateForm(request.POST)
        if form.is_valid():
            form.save()
            """
            book_name=form.cleaned_data.get("book_name")
            author=form.cleaned_data.get("author")
            price=form.cleaned_data.get("price")
            pages=form.cleaned_data.get("pages")
            obj=Book(book_name=book_name,author=author,price=price,pages=pages)
            obj.save()"""

            return redirect("listbooks")
        else:
            context={}
            context["form"] = form
            return render(request, template_name, context)

    return render(request, template_name, context)
def listbooks(request):
     template_name="listbooks.html"
     context={}
     qs =Book.objects.all()
     context["books"] = qs
     return render(request, template_name, context)
def viewbooks(request,pk):
    template_name="view.html"
    context={}
    qs=Book.objects.get(id=pk)
    context["book"]=qs
    return render(request,template_name,context)
def deletebooks(request,pk):
     Book.objects.get(id=pk).delete()
     return redirect("listbooks")
def update(request,pk):
    book=Book.objects.get(id=pk)
    form=BookCreateForm(instance=book)
    context={}
    context["form"]=form


    if request.method=="POST":
        form=BookupdateForm(instance=book,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("listbooks")

    return render(request,"update.html",context)

