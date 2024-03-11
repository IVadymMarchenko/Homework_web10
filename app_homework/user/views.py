from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth import logout
# Create your views here.





class RegisterView(View):
    template_name='user/register.html'
    form_class=RegisterForm
    def get(self,request):
        return render(request,self.template_name,context={'form':self.form_class})


    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            messages.success(request,f'Account {username} was created')
            return redirect(to='user:login')
        return render(request, self.template_name, context={'form': self.form_class})

