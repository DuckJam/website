from django.shortcuts import render
from django.http import HttpResponse
from dave.models import Page, Post, Project, Image
# Create your views here.



def index(request):
    """
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]

    context_dict = {
        'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!',
        'categories': category_list,
        'pages': page_list,
    }
    visitor_cookie_handler(request)
    """
    post_list = Post.objects.order_by('-date')[:5]
    project_list = Project.objects.order_by('-date')[:5]

    context_dict = {
        'posts':post_list,
        'projects':project_list,
    }
    response = render(request, "index.html", context= context_dict)
    return response

def about(request):
    response = render(request, "about.html")
    return response

def post(request, pk):
    context_dict ={}
    try:
        post = Post.objects.get(pk = pk)
        if post.visible:
            images = post.image.all()
            context_dict['post'] = post
            context_dict['images'] = images
            context_dict['project'] = post.project
        else:
            raise Post.DoesNotExist
    except Post.DoesNotExist:
        context_dict['post'] = None
    return render(request, 'post.html', context = context_dict)

def show_image(request, image_id):
    context_dict ={}
    try:
        image = Image.objects.get(image = image_id)
        context_dict['image'] = image
    except Post.DoesNotExist:
        context_dict['image'] = None
    return render(request, 'image.html', context = context_dict)

def project(request, project_title_slug):
    context_dict ={}
    try:
        project = Project.objects.get(slug = project_title_slug)
        posts = Post.objects.filter(project = project)
        context_dict['project'] = project
        context_dict['posts'] = posts
    except Project.DoesNotExist:
        context_dict['project'] = None
    return render(request, 'project.html', context = context_dict)
