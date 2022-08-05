from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import users
from . models import post_q
from . models import qna_db

# Create your views here.
def questions(request):
    if request.session.get('user'):
        return redirect('home')
    else:
        return render(request,'login.html')

def login(request):
    user = request.POST['user']
    upass = request.POST['upass']
    
    res = users.objects.filter(user=user, upass=upass)
    
    if len(res)==1:
        request.session['user'] = res[0].user
        return redirect('home')
    else:
        return render(request,'login.html',{'error':'Username or password is incorrect!!!'})
        
def home(request):
    if request.session.get('user'):
        return render(request,'home.html')
    else:
        return redirect('/questions/')
        
def logout(request):
    del request.session['user']
    return redirect('/questions/')

def post_question(request):
    if request.session.get('user'):
        return render(request,'post_question.html')
    else:
        return redirect('/questions/')

def post_que(request):
    pquestion = request.POST['pquestion']
    puser = request.session.get('user')
    
    res = post_q(pquestion=pquestion, puser=puser)
    res.save()
    
    return render(request,'post_question.html',{'msg':'Your question is posted successfully!!!'})

def check_qna(request):
    if request.session.get('user'):
        res = post_q.objects.all()
        return render(request,'questions.html',{'res':res})
    else:
        return redirect('/questions/')

def answers(request):
    if request.session.get('user'):
        qid = request.GET['qid']
        k = post_q.objects.filter(id=qid)
        que = k[0]
        
        ans = qna_db.objects.filter(qid=qid)
        
        return render(request,'qna.html',{'que':que,'ans':ans})
    else:
        return redirect('/questions/')

def new_ans(request):
    qid = request.POST['qid']
    answr = request.POST['answr']
    auser = request.session.get('user')
    
    res = qna_db(qid=qid, answr=answr, auser=auser)
    res.save()
    
    return redirect('check_qna')
