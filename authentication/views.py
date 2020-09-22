from django.shortcuts import render,redirect
from authentication.models import *
from authentication.forms import *
from django.http import HttpResponse
import psycopg2
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib import messages
from django.db import IntegrityError


conn = psycopg2.connect(database="reminder_website", user = "postgres", password = "jigarpinakin", host = "localhost", port = "5432")
cur = conn.cursor()

def ca_signup_view(request):
    if request.method=='GET':
        return render(request,'ca_signup.html')

    firstname= request.POST.get('firstname')
    lastname=request.POST.get('lastname')
    username=request.POST.get('username')
    email=request.POST.get('email')
    password=request.POST.get('password') 
    # ca_name= request.user.get_full_name()
    # Create user and save to the database
    ca_user = User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=username,password=password,is_staff='True')
    ca_user.save()
    
    return redirect('../ca_login')
    
   

def staff_signup_view(request):
    if request.method=='GET':
        return render(request, 'staff_signup.html')
    print(request.POST)
    print(request.method)
    print(request.POST.get('firstname'))
    firstname= request.POST.get('firstname')
    lastname=request.POST.get('lastname')
    username=request.POST.get('username')
    phone=request.POST.get('phone')
    ca_name=request.POST.get('ca_name')
    email=request.POST.get('email')
    password=request.POST.get('password') 
    repass=request.POST.get('repass')  
    
    # print('signup_view')
    
    # Create user and save to the database
    u1 = User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=username,password=password)
    
    sign_obj =StaffModel(staff=u1,ca_name=ca_name,phone_no=phone,repassword=repass)  
    u1.save()
    sign_obj.save()
    return redirect('../staff_login')

def ca_login_view(request):
    if request.method=='GET':
        return render(request,'ca_login.html')
      
    email_user_input= request.POST.get('email')
    pass_user_input = request.POST.get('password')
    print(email_user_input)
    print(pass_user_input)
    username= User.objects.get(email=email_user_input)
    print(username)
    print("=="*50)
    user = authenticate(request,username=username, password=pass_user_input)
    print(user)
    query="SELECT is_staff FROM public.auth_user WHERE username='"+str(username)+"'"
    cur.execute(query)
    rows=cur.fetchall()
    print(rows[0][0])
    if user is not None and rows[0][0]:
        login(request, user)
        return redirect('../ca_dashboard/')
    else:
        return HttpResponse("Your username and password didn't match.")
    
def staff_login_view(request):
    if request.method=='GET':
        return render(request,'staff_login.html')
      
    email_user_input= request.POST.get('email')
    pass_user_input = request.POST.get('password')
    print(email_user_input)
    print(pass_user_input)
    username= User.objects.get(email=email_user_input)
    print(username)
    print("=="*50)
    user = authenticate(request,username=username, password=pass_user_input)
    print(user)
    
    query="SELECT is_staff FROM public.auth_user WHERE username='"+str(username)+"'"
    cur.execute(query)
    rows=cur.fetchall()
    print(rows[0][0])
    if user is not None and rows[0][0]==False:
        login(request, user)
        return redirect('../staff_dashboard/')
    else:
        return HttpResponse("Your username and password didn't match.")
    


def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect('../../../../../../')