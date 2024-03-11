from django.shortcuts import render
from .models import Quote,Author
from django.core.paginator import Paginator

# Create your views here.

def main(request,page=1):
    quote_list = Quote.objects.all()
    author_ids = set(quote.author_id for quote in quote_list)
    authors = Author.objects.filter(id__in=author_ids)
    per_page=10
    paginator=Paginator(list(quote_list),per_page)
    quote_on_page=paginator.page(page)
    return render(request, 'quotes/index.html', {'quotes_list': quote_on_page, 'authors': authors})


def author_data(request,author_id):
    author=Author.objects.get(id=author_id)
    return render(request,'quotes/author_detail.html', {'author': author})


