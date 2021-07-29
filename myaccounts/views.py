from myaccounts.models import Myuser
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model,login as django_login,authenticate as django_authenticate,logout as django_logout

from myaccounts.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
#print(make_password('123'))
# Create your views here.
def create_new_user(request):
    if request.method == 'POST':
        ut_name = request.POST['ut_name']
        prenom = request.POST['prenom']
        passuser = request.POST['passuser']
        user_model = get_user_model()
        user_obj =  user_model.objects.create_user(ut_name=ut_name,prenom=prenom,passuser=make_password(passuser))
        #user_obj.set_password(passuser)
        user_obj.save()
    else:
        return render(request,'myaccounts/create_new_user.html')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            ut_name = request.POST['ut_name']
            passuser = request.POST['passuser']
            #user = django_authenticate(ut_name=ut_name, passuser=make_password(passuser))
            try:
                user1 = Myuser.objects.get(ut_name=ut_name)
                #return HttpResponse(user)
            except Myuser.DoesNotExist:
                form = AuthenticationForm()
                return render(request,'myaccounts/login.html',{'form':form,'msg':'jjjjjjjj'})
                #return redirect('myaccounts:login')
            if user1 is not None and check_password(passuser, user1.passuser):
                #if user.is_active and check_password(passuser, user.passuser):
                django_login(request,user1)
                return redirect('myapp:index') #user is redirected to dashboard
    else:
        form = AuthenticationForm()
    return render(request,'myaccounts/login.html',{'form':form,})

def logout(request):
    django_logout(request)
    return redirect('myaccounts:login')

