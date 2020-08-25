from django.shortcuts import render, redirect
from .models import Stock, Entry
from .forms import StockForm, EntryForm


def index(request):
    """The homepage for Stock Tracker."""
    return render(request, 'stock_trackers/index.html')

def stocks(request):
    """Show all stocks."""
    stocks= Stock.objects.order_by('date_added')
    context= {'stocks': stocks}
    return render(request, 'stock_trackers/stocks.html', context)

def stock(request, stock_id):
    """Show a single stock and all its notes."""
    stock= Stock.objects.get(id=stock_id)
    entries= stock.entry_set.order_by('-date_added')
    context= {'stock': stock, 'entries': entries}
    return render(request, 'stock_trackers/stock.html', context)

def new_stock(request):
    """Add a new stock."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form= StockForm()
    else:
        # POST data submitted; process data.
        form= StockForm(data=request.POST)
        if form.is_valid():
            new_stock= form.save(commit=False)
            new_stock.save()
            return redirect('stock_trackers:stocks')
    #Display a blank or invalid form.
    context= {'form': form}
    return render(request, 'stock_trackers/new_stock.html', context)

def new_entry(request, stock_id):
    """Add notes for a specific stock."""
    stock= Stock.objects.get(id= stock_id)
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form= EntryForm()
    else:
        # POST data submitted; process data.
        form= EntryForm(data= request.POST)
        if form.is_valid():
            new_entry= form.save(commit= False)
            new_entry.stock= stock
            new_entry.save()
            return redirect('stock_trackers:stock', stock_id= stock_id)

    # display a blank or invalid form
    context= {'stock':stock, 'form': form}
    return render(request, 'stock_trackers/new_entry.html', context)

def edit_entry(request, entry_id):
    """Edit an exiting note."""
    entry= Entry.objects.get(id= entry_id)
    stock= entry.stock

    if request.method != 'POST':
        #initial request; pre-fill form with the current note entry.
        form= EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form= EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('stock_trackers:stock', stock_id=stock.id)

    context= {'entry': entry, 'stock': stock, 'form': form}
    return render(request, 'stock_trackers/edit_entry.html', context)












