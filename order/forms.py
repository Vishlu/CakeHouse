from django import forms
from .models import Userinformation




class Order(forms.ModelForm):

    LOCATION = [
        ('kandivali', 'Kandivali'),
        ('borivali', 'Borivali'),
    ]

    CAKE = [
        ('venila Cake - ₹ 399','Venila Cake - ₹ 399'),
        ('white Milk Straw-berry Cake - ₹ 349', 'White Milk Straw-berry Cake - ₹ 349'),
        ('dark Three-Layer Chocolate Cake - ₹ 1099', 'Dark Three-Layer Chocolate Cake - ₹ 1099'),
        ('dark Two-Layer Chocolate Cake - ₹ 999', 'Dark Two-Layer Chocolate Cake - ₹ 999'),
        ('dark Five-Layer Chocolate Cake - ₹ 1699', 'Dark Five-Layer Chocolate Cake - ₹ 1699'),
        ('dark Two-Layer ice-cream Cake - ₹ 299', 'Dark Two-Layer ice-cream Cake -₹ 299'), 
        ('pink Straw-berry Cake - ₹ 649', 'Pink Straw-berry Cake - ₹ 649'), 
        ('white Straw-berry Cake - ₹ 749', 'White Straw-berry Cake - ₹ 749'),
        ('dark Straw-berry Chocolate Cake - ₹ 549', 'Dark Straw-berry Chocolate Cake - ₹ 549')
    ]

    user_name = forms.CharField(error_messages={'required': 'Please Enter Your Valid Name.'}, widget=forms.TextInput(attrs={'placeholder': 'Enter Your Name.', 'max_length': 50, 'class':'form-control w-25'}))
    first_name = forms.CharField(error_messages={'required': 'Enter Your First Name.'}, widget=forms.TextInput(attrs={'placeholder': 'Enter Your Name.', 'max_length': 50, 'class':'form-control w-25'}))
    location = forms.CharField(widget=forms.Select(choices=LOCATION, attrs={'class': 'form-control w-25'}))
    phone_no = forms.IntegerField(error_messages={'required': 'Only ten Numbers must be includes.'}, widget=forms.NumberInput(attrs={'class': 'form-control w-25', 'placeholder': 'Enter Your Phone No.'}))
    cake = forms.CharField(widget=forms.Select(choices=CAKE, attrs={'class': 'form-control w-25'}))
    quantity = forms.IntegerField(error_messages={'required': 'Quantity is required.'}, widget=forms.NumberInput(attrs={'placeholder': 'Add Your Quantity', 'class': 'form-control w-25'}))

    def clean(self):
       # cleaned_data = super().clean()
        valuser_name = self.cleaned_data.get('user_name')
        valfirst_name = self.cleaned_data.get('first_name')
        if valuser_name !=  valfirst_name:
            raise forms.ValidationError('Your Name Does Not Matched.')

    class Meta:

        model = Userinformation

        fields = ['user_name', 'first_name', 'last_name','email_id', 'phone_no', 'address', 'location', 'cake', 'quantity']

        labels = {'user_name':'Username :', 'first_name': 'First Name :', 'last_name':'Last Name :', 'email_id': 'Email-ID :', 'phone_no': 'Phone no:', 'address': 'Address', 'location': 'Location'}
  
        error_messages = {
          #  'user_name':{'required': 'Please Enter Your Valid Name.'},
          #  'first_name':{'required': 'Enter Your First Name.'},
            'last_name':{'required': 'Enter Your Last Name.'},
            'email_id':{'required': 'Enter Your Valid Email Address.'},
          #  'phone_no':{'required': 'Only ten Numbers must be includes.'},
            'address':{'required': 'User address Must be Compulsory.'},
            'location':{'required': 'Your Location is required'},
            
        }
        widgets = {
            #'user_name': forms.TextInput(attrs={'class': 'user_name', 'placeholder': 'Enter Your Name',}),
            #'first_name': forms.TextInput(attrs={'class': 'first_name', 'placeholder': 'Enter Your First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control w-25', 'placeholder': 'Enter Your Last Name',}),
            'email_id': forms.EmailInput(attrs={'class': 'form-control w-25', 'placeholder': 'Enter Your Email-id'}),
           # 'phone_no': forms.NumberInput(attrs={'class': 'phone', 'placeholder': 'Enter Your Phone No.', 'min_value':10}),
            'address': forms.Textarea(attrs={'class': 'form-control w-25','rows': 8, 'cols': 50, 'placeholder': 'Enter Your Valid Address.'}),
            'location': forms.TextInput(attrs={'class': 'form-control w-25'}),
        }
