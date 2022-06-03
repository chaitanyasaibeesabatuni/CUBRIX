from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customers import Customer
from django.views import View

class Signup(View):
    def get(self,request):
        return render(request, 'signup.html')
    def post(self,request):
        s = request.POST
        firstname = s.get('firstname')
        lastname = s.get('lastname')
        mobile = s.get('mobile')
        email = s.get('email')
        password = s.get('password')
        customer = Customer(firstname=firstname,
                            lastname=lastname,
                            mobile=mobile,
                            email=email,
                            password=password)
        value = {
            'firstname': firstname,
            'lastname': lastname,
            'mobile': mobile,
            'email': email
        }
        error_message = self.validation(customer)
        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)
    def validation(self,customer):
        error_message = None
        if not customer.email:
            error_message = 'Email must be Required'
        elif not customer.mobile:
            error_message = 'Mobile Number must be Required'
        elif not customer.firstname:
            error_message = 'First Name Required !!!'
        elif not customer.lastname:
            error_message = 'Last Name Required'
        elif len(customer.firstname) < 3:
            error_message = 'First Name must be 5 char long or more'
        elif not customer.password:
            error_message = 'Password must be Required !!!!!!!!!!!'
        elif len(customer.password) < 5:
            error_message = 'Your password is weak , include special characters,numbers and caps'
        elif len(customer.mobile) < 10:
            error_message = 'Invalid Number'
        elif customer.isExist():
            error_message = 'Email is already registered '
        return error_message
