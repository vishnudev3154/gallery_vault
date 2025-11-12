from django.shortcuts import render,redirect
import bcrypt
from . models import *
def regster(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        age=request.POST['age']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if password==cpassword:
            hashed_pw=bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            data=register.objects.create(name=name, email=email, age=age, password=hashed_pw)
            data.save()
            print(data)
            return redirect(userlogin)
    return render(request, 'index.html')

def userlogin(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        try:
            user=register.objects.get(email=email)
            if bcrypt.checkpw(password.encode('utf-8'),user.password.encode('utf-8')):
                request.session['user']=user.id
                return redirect(home)
        except:
            print('user not found')
            
    return render(request, 'login.html')

# def userpage(request):
#     if 'user' in request.session:
#         user=register.objects.get(pk=request.session['user'])
#         return render(request,'user.html',{'user':user})
    
#     return render(request, 'user.html')

def home(request):
    
    if 'user' in request.session:
        user = register.objects.get(pk=request.session['user'])
        files = Files.objects.filter(user=user)
        return render(request, 'user.html', {'user': user, 'files': files})
    else:
        return redirect(userlogin)
    



def addfile(request):
    if 'user' in request.session:
        if request.method == 'POST':
            title = request.POST['title']
            file = request.FILES.get('doc')
            user = register.objects.get(pk=request.session['user'])
            data = Files.objects.create(user=user, title=title, file=file)
            data.save()
            return redirect(home)
        return render(request, 'addfile.html')
    else:
        return redirect(home)
