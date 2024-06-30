from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from . models import Movie
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def index(request):
    movies = Movie.objects.all()
    
    context= {
        'movies': movies
    }
    return render(request, 'index.html', context)

@login_required(login_url='login')
def movie(request, pk):
    movie_uuid=pk
    movie_details=Movie.objects.get(uu_id=movie_uuid)
    
    context={
        'movie_details': movie_details
    }
    return render(request, 'movie.html',context)

def my_list(request):
    pass

def add_to_list(request):
    pass

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials...')
            return redirect('login')
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken...')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken...')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                #Giriş yapma
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)
                return redirect('/')
        else:
            messages.info(request, 'Password not matching...')
            return redirect('signup')
    else:
        return render(request, 'signup.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')    