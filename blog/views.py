from django.shortcuts import render, get_object_or_404
from . models import Blog, Tag
# Create your views here.


def blog_list(request):
    blogs = Blog.objects.all()

    context = {
        "blogs": blogs
    }

    return render(request, "blog/blog_list.html", context)


def blog_detail(request, id):
    blog = Blog.objects.get(id=id)
    tags = Tag.objects.all().filter(blogs=blog)
    recent = Blog.objects.all().order_by("-creates_at")[:5]
    context = {
        "blog": blog,
        "tags": tags,
        recent: recent
    }
    return render(request, "blog/blog_detail.html", context)
