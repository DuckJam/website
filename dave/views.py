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
    post_list = Post.objects.order_by('-date')[:3]
    image_list = Image.objects.order_by('name')[:3]

    context_dict = {
        'posts':post_list,
        'images':image_list,
    }
    response = render(request, "index.html", context= context_dict)
    return response

def about(request):
    response = render(request, "about.html")
    return response

def show_post(request, pk):
    context_dict ={}
    try:
        post = Post.objects.get(pk = pk)
        images = post.image.all()
        context_dict['post'] = post
        context_dict['images'] = images
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

