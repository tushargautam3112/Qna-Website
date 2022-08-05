from django.shortcuts import render
from questions.models import users

# Create your views here.
def signup(request):
    return render(request,'signup.html')
    
def account(request):
    sname = request.POST['sname']
    user = request.POST['user']
    upass = request.POST['upass']
    
    res = users.objects.filter(user=user)
    
    if len(res)>0:
        return render(request,'signup.html',{'msg':'This user name is already taken!!!'})
    else:
        q = users(sname=sname, user=user, upass=upass)
        q.save()
        return render(request,'signup.html',{'msg':'Account Created Successfully!!!'})
        
        
        
        
        