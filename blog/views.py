from django.shortcuts import render , HttpResponse,redirect
from .models import Post ,Blogcomment
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q

from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.core.paginator import Paginator

# Create your views here.

def blogHome(request):
    allpost = Post.objects.all().order_by('-timestamp')
    paginator = Paginator(allpost,3)
    page_number = request.GET.get('page')
    page_obj =paginator.get_page(page_number)
    context = {'page_obj': page_obj }
    return render(request,'blog/blog.html',context)

def blogPost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    post.views = post.views + 1
    post.save()
    comments = Blogcomment.objects.filter(post=post , parent=None)
    replies = Blogcomment.objects.filter(post=post ).exclude(parent=None) #because we cannot write != directly in django
    replyDict ={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)


    context = {'post':post ,'comments':comments , "user" : request.user,'replyDict':replyDict}
    return render(request, 'blog/blogpost.html',context)

def search(request):
    query = request.GET['query']
    if len(query)>80:
        allpost = Post.objects.none()
    else:
        allpost = Post.objects.filter( Q(title__icontains=query) |
        Q(content__icontains=query) | Q(author__icontains=query)
        | Q(slug__icontains=query) )
        
        
        
    if allpost.count() == 0:
        messages.warning(request,"No search result found. Please refine your query")
    params = {'allpost':allpost,'query':query}
    return render(request,'blog/search.html',params)

def handlesignup(request):
    if request.method =='POST':
        username = request.POST.get('username')
        fname = request.POST.get('userfirstname')
        lname = request.POST.get('userlastname')
        email = request.POST.get('useremail')
        password = request.POST.get('userpassword')
        cpassword = request.POST.get('usercpassword')

        if not username:
            messages.error(request," Username Required")
        elif len(username) < 4:
            messages.error(request," Username must be under characters")
        elif User.objects.filter(username=username).exists():
            messages.error(request," Already User exist. Try Another username")
        elif not fname:
            messages.error(request," First Name Required !!")
        elif len(fname) < 3 or len(fname) > 10:
            messages.error(request,' First Name must be 4 char long or more')
        elif not lname:
            messages.error(request,' Last Name Required..')
        elif len(lname) < 4 or len(lname) > 10:
            messages.error(request,' Last Name must be 4 char long or more')
        elif len(email) < 5 or len(email) < 16:
            messages.error(request,'Email must be 5 char long')
        elif User.objects.filter(email=email).exists():
            messages.error(request," Email Already exist. Try Another Email")
        elif not password:
            messages.error(request," Password Required")
        elif not cpassword:
            messages.error(request," Confirm Password Required")
        elif len(password) < 6 or len(password) > 20:
            messages.error(request,' Password must be 6 char long')
        elif password != cpassword:
            messages.error(request," Password do not match")
            
        else:
            
            myuser = User.objects.create_user(username,email,password)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()

            user = authenticate(username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                messages.error(request,"Invalid Credentials, Please try again")
            
            messages.success(request," Account has been sucessfully created")

        return redirect('/')
    else:
        return HttpResponse(request,'404')


def handlelogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername,password=loginpassword)

        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentials, Please try again")
            return redirect('/')


def handlelogout(request):
    # if request.method == 'POST':
    logout(request)
    return redirect('home')

def postComment(request):
    if request.method == "POST":
        comment = request.POST.get("comments")
        user = request.user
        postSno = request.POST.get("postSno")
        post = Post.objects.get(sno=postSno)
        parentSno = request.POST.get('parentsno')
        if parentSno == "" :
            comments = Blogcomment(comment=comment,user=user ,post=post)
            comments.save()
            messages.success(request," Comment Posted Sucessfully")
        else :
            parent = Blogcomment.objects.get(sno=parentSno)
            comments = Blogcomment(comment=comment,user=user ,post=post ,parent=parent)
            comments.save()
            messages.success(request," Reply Posted Sucessfully")
    return redirect(f"/blog/{post.slug}")


