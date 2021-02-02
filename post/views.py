from django.shortcuts import render,get_object_or_404,HttpResponseRedirect,redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.




def index(request):

    posts=Post.objects.all().order_by('-id')
    query=request.GET.get('search')
    if query:
        


        posts=posts.filter(Q(title__icontains=query))




    paginator = Paginator(posts, 2) # Show 25 contacts per page.

    page = request.GET.get('page')
    posts = paginator.get_page(page)



    return render(request,'index.html',{'posts':posts})


def detail_view(request,id):

    posts=Post.objects.get(id=id)

    return render(request,'detail.html',{'posts':posts})



@login_required(login_url='index')
def create_view(request):

    form=PostForm(request.POST or None , request.FILES or None)
    if form.is_valid():
        post=form.save()
        return HttpResponseRedirect(post.get_absolute_url())

    return render(request,'create.html',{'form':form})


@login_required(login_url='index')
def delete_view(request,id):

    posts=get_object_or_404(Post,id=id)
    posts.delete()
    return redirect('index')




def update_view(request,id):

    posts=Post.objects.get(id=id)
    form=PostForm(request.POST or None,request.FILES or None,instance=posts)

    if form.is_valid():
        posts.save()
        return HttpResponseRedirect(posts.get_absolute_url())

    return render(request,'create.html',{'form':form})
