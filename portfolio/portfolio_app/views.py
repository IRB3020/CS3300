from django.shortcuts import render
from django.http import HttpResponse


# Create Views Here.
def index(request):
    # Render HTML Template w/Context Variable
    return render(request, 'portfolio_app/index.html')
