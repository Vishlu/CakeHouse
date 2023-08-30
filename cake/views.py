from django.shortcuts import render

# Create your views here.
def cake(request):
    return render(request, 'cake/cake.html')