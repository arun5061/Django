from django import forms
from product_details.models import productModel

class productForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Titile"}))
    description = forms.CharField(required=False,widget=forms.Textarea(attrs={"placeholder":"Description",
                                                                              "rows":20,
                                                                              "cols":40}))
    class Meta:
       model = productModel
       fields = [
               'title',
               'description',
               #'price'
           ]
    #Form Validations
    #Syntax  def clean_<fieldName>
