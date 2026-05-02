from django import forms
from . models import item

class ItemForm(forms.ModelForm):
    class Meta:
        model = item
        fields =['item_name','item_price','item_desc','item_image']

        widgets={
            'item_name':forms.TextInput(attrs={"placeholder":"e.g. Pizza","required":True}),
            'item_price':forms.NumberInput(attrs={"placeholder":"e.g. 9.99","required":True}),
            'item_desc':forms.Textarea(attrs={"placeholder":"e.g. Delicious pizza with cheese and pepperoni","required":True}),
            'item_image':forms.URLInput(attrs={"placeholder":"e.g. https://example.com/pizza.jpg","required":True}),
        }

    def clean_item_price(self):
        price = self.cleaned_data.get('item_price')
        if price <= 0:
            raise forms.ValidationError("Price must be greater than zero.")
        return price
    

    def clean(self):
        cleaned = super().clean()
        name = cleaned.get('item_name')
        desc = cleaned.get('item_desc')
        if name and desc and name.lower() in desc.lower():
            self.add_error('item_desc', "Description should not contain the item name.")