from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from users.forms import UserForm
from users.models import User

# Create your views here.
class MainView(View):
    template = 'index.html'

    def get(self,request):
        return render(request,self.template)

class LogInView(View):
    template = 'users/log_in.html'
    form_class = UserForm

    def get(self, request):
        return render(request, self.template,{'form':form_class()})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        users = User.objects.all().filter(username=username)
        if len(users) == 1 and check_password(password,users[0].password):
            return redirect("users/")
 

class RegisterView(View):
    template = 'users/register.html'
    form_class = UserForm

    def get(self, request):
        return render(request, self.template,{'form':form_class()})

    def post(self, request):
        user_info = self.form_class(request.POST)
        if user_info.is_valid():
            user = user_info(commit=False)
            user.password = make_password(user.password)
            user.save()
            request.session['user_id'] = user.id
            return redirect("users/")
