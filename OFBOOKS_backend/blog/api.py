from django.http import JsonResponse
from django.db.models import Q
from functools import reduce

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from account.models import User
from account.serializers import UserSerializer

from book.models import Book, Tag
from book.serializers import BookSerializer

# from .forms 
from .models import Paragraph, Blog, Tag, Like
from .serializers import BlogSerializer, \
    BlogDetailSerializer, \
    TagSerializer


@api_view(['GET'])
def like(request, id):
    blog = Blog.objects.get(pk=id)
    user = User.objects.get(pk=request.user.id)
    newLike, is_new = Like.objects.get_or_create(created_by=user, created_for=blog)
    if not is_new:
        newLike.delete()
    
    like_count = blog.like_count()

    return JsonResponse({'like_count': like_count, 'is_liked': is_new}, safe=False)


@api_view(['GET'])
@permission_classes([])
def trend_tags(request):
    tags = Tag.objects.filter(is_trend=True)
    
    tags_serializer = TagSerializer(tags, many=True)

    return JsonResponse(tags_serializer.data, safe=False)


@api_view(['POST'])
@permission_classes([])
def get_feed(request):
    keywords        = request.data.get('keywords')
    tag_id          = request.data.get('tag_id')
    sort_by         = request.data.get('sort_by')
    idx             = request.data.get('idx', 0)

    blogs           = Blog.objects.all()

    if tag_id:
        blogs = blogs.filter(Q(
            tags=tag_id
        ))
    
    if keywords:
        blogs = blogs.filter(
            Q(title__icontains=keywords) | 
            Q(description__icontains=keywords) |
            Q(paragraphs__title__icontains=keywords) |
            Q(paragraphs__body__icontains=keywords)
        ).distinct()
    
    match sort_by:
        case 'new':
            blogs = blogs.order_by('-created_at')
        case 'popular':
            tags = Tag.objects.filter(is_trend=True)
            blogs = blogs.filter(
                Q(tags__in=tags)
            ).distinct()
        case 'view':
            ...

    blogs = blogs[0:idx + 4]
    
    blogs_serializer = BlogSerializer(blogs, many=True, context={'user_id': request.user.id})


    return JsonResponse(blogs_serializer.data, safe=False)


@api_view(['POST'])
@permission_classes([])
def blog_detail(request, id):
    blog = Blog.objects.get(pk=id)
    tags = Tag.objects.filter(blogs=blog)

    blog_serializer = BlogDetailSerializer(blog, context={'user_id': request.user.id})
    
    if len(tags) > 0:

        querySet = reduce(lambda a, b: a | b, [
            Q(tags=tag)
            for tag in tags
        ])

        books = Book.objects.filter(querySet).distinct()[:request.data.get('book_index') + 4]
        blogs = Blog.objects.filter(querySet).exclude(id=id).distinct()[:request.data.get('blog_index') + 4]
        
        blogs_serializer = BlogDetailSerializer(blogs, context={'user_id': request.user.id}, many=True)
        books_serializer = BookSerializer(books, read_only=True, many=True)

    else:
        return JsonResponse({
        'blog': blog_serializer.data,
    }, safe=False)


    return JsonResponse({
        'blog': blog_serializer.data,
        'blogs': blogs_serializer.data,
        'books': books_serializer.data,
    }, safe=False)


@api_view(['POST'])
@permission_classes([])
def myBlogs(request):
    my_idx, suggestion_idx = request.data['my_idx'], request.data['suggestion_idx']
    user = User.objects.get(pk=request.user.id)
    my_blogs = user.blogs.order_by('-created_at')[:my_idx + 4]
    suggestion = Blog.objects.all()[:suggestion_idx + 4]
    
    my_blogs_serializer = BlogSerializer(my_blogs, many=True, context={'user_id': request.user.id},)
    suggestion_serializer = BlogSerializer(suggestion, many=True, context={'user_id': request.user.id})

    return JsonResponse({
        'my_blogs': my_blogs_serializer.data,
        'suggestion': suggestion_serializer.data,
    }, safe=False)
    
