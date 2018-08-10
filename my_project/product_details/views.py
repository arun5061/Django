from django.shortcuts import render, redirect
from django.http import HttpResponse
from product_details.forms import productForm
from product_details.models import productModel
from django.views.generic import ListView
# Create your views here.
def create_product(request):
    #To pass initial values to form - Declare a dictionary with required fileds and pass a INITIAL
    #We can pass DB variables as "instance" to initialize fields
    #obj = productModel.objects.get(pk=73)
    form = productForm()
    context = {'form':form}
    return render(request, "product_details/product_createForm.html", context )
def submit_product(request):
    form = productForm(request.POST or None)
    print(request.POST)
    if form.is_valid():
        #obj = productModel(title=request.POST['title'])
        #obj2 = productModel(description=request.POST['description'])
        #obj.save()
        form.save()
        print("Valid Form")
    return redirect('create')
class Product_View(ListView):
    queryset = productModel.objects.all()
