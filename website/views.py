from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'login.html', {})

def home(request):
    return render(request, 'home.html', {})

def dashboard(request):
    tweets =[]
    tweets.append(('dvhsdf', 'Bully'))
    tweets.append(('sjhdfgh', 'Not Bully'))
    tweets.append(('svdsjhdfuey', 'Bully'))
    tweets.append(('dvhsdf', 'Bully'))
    tweets.append(('sjhdfgh', 'Not Bully'))
    tweets.append(('svdsjhdfuey', 'Bully'))
    tweets.append(('dvhsdf', 'Bully'))
    tweets.append(('sjhdfgh', 'Not Bully'))
    tweets.append(('svdsjhdfuey', 'Bully'))
    tweets.append(('dvhsdf', 'Bully'))
    tweets.append(('sjhdfgh', 'Not Bully'))
    tweets.append(('svdsjhdfuey', 'Bully'))
    return render(request, 'dashboard.html', {'tweets':tweets})