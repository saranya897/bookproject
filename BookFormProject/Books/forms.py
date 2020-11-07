from Books.models import Book
from django import forms
from django.forms import ModelForm

"""class BookCreateForm(forms.Form):
    book_name=forms.CharField(max_length=120)
    author=forms.CharField(max_length=120)
    price=forms.IntegerField()
    pages=forms.IntegerField()
    """
class BookCreateForm(forms.ModelForm):
    class Meta:
        model=Book
        fields="__all__"


    def clean(self):
        clean_data=super().clean()
        book_name=clean_data.get('book_name')
        price = clean_data.get('price')
        book=Book.objects.filter(book_name=book_name)

        if book:
            msg="book already exist"
            self.add_error('book_name',msg)
        if price<0:
            msg="negative price"
            self.add_error('price', msg)
class BookupdateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"