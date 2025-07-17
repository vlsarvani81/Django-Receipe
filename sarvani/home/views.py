from django.shortcuts import render,redirect
from .models import *
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import FeedbackForm
def home(request):
    if 'page_count' not in request.session:
        request.session['page_count'] = 0
    request.session['page_count'] += 1
    stu=[{"name": "Tom", "age": 20},{"name": "Mark", "age": 5},  {"name": "Pam", "age": 7}]
    response= render(request,"index.html",context={'stu':stu,'page_count': request.session['page_count']})
    response.delete_cookie('token')
    return response
   

def success(request):
    return HttpResponse("<h1>hey iam in success page</h1>")
def about(request):
    response= render(request,"about.html")
    response.set_cookie('token','t123456',max_age=3600)
    return response

def contact(request):
    token = request.COOKIES.get('token')
    return render(request,"contact.html",{'token':token})

@login_required(login_url='/login/')
def receipes(request):
    if request.method == "POST":
        data=request.POST
        ri=request.FILES.get('ri')
        rn=data.get('rn')
        rd=data.get('rd')
        Receipe.objects.create(
        rn=rn,
        rd=rd,
        ri=ri,)
        return redirect('/receipes/')
    queryset = Receipe.objects.all()
    context={'receipes':queryset}
    return render(request,'receipes.html',context)

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('un')  
        password = request.POST.get('psw')  
        
        print(f"Username: {username}, Password: {password}")  # Debugging line
        
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, 'Invalid username or password')
            return redirect('/login/')
        else:
            login(request, user)  # Pass the request and user
            return redirect('/receipes/')

    return render(request, 'login.html')
def logout_page(request):
    request.session.pop('page_count', None)
    logout(request)
    return redirect('/login/')
def register(request):
    if request.method == "POST":
        first_name = request.POST.get('fn')
        last_name = request.POST.get('ln')
        username = request.POST.get('run')
        password = request.POST.get('rpsw')
        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request, "username already exists")
            return redirect("/register/")
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        user.set_password(password)
        user.save()
        messages.info(request,"account created successfully")
        return redirect('/login/')
    return render(request, 'register.html')

def student_feedback(request):
    if request.method == 'POST':  
        form = FeedbackForm(request.POST) 
        if form.is_valid():        
            form.save()            
            return redirect('/feedback/') 
    else:                         
        form = FeedbackForm()      
    return render(request, 'feedback_form.html', {'form': form}) 
