from django.shortcuts import render

# Create your views here.

from .models import Book, Author, BookInstance, Genre

def index(request):
    """
    view function for home page of site
    """
    # Genereate the counts of some of the main objects
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    # Available Books(status = 'a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count() # The all()' is implied by default '

    num_genres=Genre.objects.count()
    num_books_1q84=BookInstance.objects.filter(book__title__exact='1Q84').count()



    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_instances':num_instances, 'num_instances_available':num_instances_available, 'num_authors': num_authors, 'num_books_1q84': num_books_1q84},
    )

from django.views import generic

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 2

class BookListView(generic.ListView):
    model = Book
    paginate_by = 2 
    # context_boject_name = 'my_book_list'
    # queryset = Book.objects.filter(title__icontains='war')[:5]
    # template_name = 'books/my_arbitrary_template_name_list.html'

    # def get_queryset(self):
        # return Book.objects.filter(title__icontains='war')[:5]

    # def get_context_data(self, **kwargs):
        # """
        # call the base implementation first to get a context
        # """
        # context = super(BookListView, self).get_context_data(**kwargs)
        # context['some_data'] = 'this is some data'
        # return context

class AuthorDetailView(generic.DetailView):
    model = Author

class BookDetailView(generic.DetailView):
    model = Book

def author_detail_view(request,pk):
    try:
        author_id=Author.objects.get(pk=pk)
    except Author.DoesNotExist:
        raise Http404("Author does not exist")

    return render(
        request,
        'catalog/author_detail.html',
        context={'author': author_id,}
    )

def book_detail_view(request,pk):
    try:
        book_id=Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")

    #book_id=get_object_or_404(Book, pk=pk)
    
    return render(
        request,
        'catalog/book_detail.html',
        context={'book':book_id,}
    )

# def book_detail_view(request,pk):
    # try:
        # book_id=Book.objects.get(pk=pk)
    # except Book.DoesNotExist:
        # raise Http404("Book does not exist")

    # #book_id=get_object_or_404(Book, pk=pk)
    
    # return render(
        # request,
        # 'catalog/book_detail.html',
        # context={'book':book_id,}
    # )

