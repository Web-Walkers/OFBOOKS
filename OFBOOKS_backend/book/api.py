from django.http import JsonResponse
from django.db.models import Q, Count
from functools import reduce

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from account.models import User
from account.serializers import UserSerializer

from blog.models import Tag

# from .forms 
from .models import Book, \
                    Publishing_Company, \
                    Author, \
                    Interpreter, \
                    Subject, \
                    Genre, \
                    Achievement, \
                    Literature
from .serializers import SubjectSerializer, SubjectDetailSerializer, \
                            BookSerializer, BookDetailSerializer, \
                            PublishingCompanySerializer, PublisherDetailSerializer, \
                            LiteratureSerializer, LiteratureDetailSerializer


@api_view(['GET'])
@permission_classes([])
def get_literatures(request):
    literatures = Literature.objects.all()
    
    literatures_serializer = LiteratureSerializer(literatures, many=True)

    return JsonResponse(literatures_serializer.data, safe=False)


@api_view(['GET'])
@permission_classes([])
def literature_detail(request, id):
    literature = Literature.objects.get(pk=id)
    
    literature_serializer = LiteratureDetailSerializer(literature)

    return JsonResponse(literature_serializer.data, safe=False)


@api_view(['GET'])
@permission_classes([])
def get_publishers(request):
    publishers = Publishing_Company.objects \
        .annotate(b_count=Count('books')) \
        .order_by('-b_count')[:8]
    
    publishers_serializer = PublishingCompanySerializer(publishers, many=True)

    return JsonResponse(publishers_serializer.data, safe=False)


@api_view(['GET'])
@permission_classes([])
def publisher_detail(request, id):
    publisher = Publishing_Company.objects.get(pk=id)
    
    publisher_serializer = PublisherDetailSerializer(publisher)

    return JsonResponse(publisher_serializer.data, safe=False)


@api_view(['GET'])
@permission_classes([])
def get_subjects(request):
    subjects = Subject.objects.all()
    
    subjects_serializer = SubjectSerializer(subjects, many=True)

    return JsonResponse(subjects_serializer.data, safe=False)


@api_view(['GET'])
@permission_classes([])
def subject_detail(request, id):
    subject = Subject.objects.get(pk=id)
    
    subject_serializer = SubjectDetailSerializer(subject)

    return JsonResponse(subject_serializer.data, safe=False)


@api_view(['GET'])
@permission_classes([])
def get_best_subjects(request):
    subjects = Subject.objects \
        .annotate(b_count=Count('books')) \
        .order_by('-b_count')[:4]
    
    subjects_serializer = SubjectDetailSerializer(subjects, many=True)

    return JsonResponse(subjects_serializer.data, safe=False)


@api_view(['POST'])
@permission_classes([])
def get_feed(request):

    #┌──────────────────────────────────────────┐
    #│                   Data                   │
    #└──────────────────────────────────────────┘
    data = request.data
    keywords        = data.get('keywords', '')
    subject_id      = data.get('subject_id', '')
    publisher_id    = data.get('publisher_id', '')
    literature_id   = data.get('literature_id', '')
    sort_by         = data.get('sort_by', 'new')
    idx             = data.get('idx', 0)


    #┌──────────────────────────────────────────┐
    #│                Query-Set                 │
    #└──────────────────────────────────────────┘
    books = Book.objects.all()


    #┌──────────────────────────────────────────┐
    #│                  Filter                  │
    #└──────────────────────────────────────────┘
    if subject_id:
        books = books.filter(Q(
            subject=subject_id
        ))
        
    if publisher_id:
        books = books.filter(Q(
            publisher=publisher_id
        ))
        
    if literature_id:
        books = books.filter(Q(
            literature=literature_id
        ))
    
    if keywords:
        books = books.filter(Q(
            name__icontains=keywords
        ))
    


    #┌──────────────────────────────────────────┐
    #│                  Sort-By                 │
    #└──────────────────────────────────────────┘
    match sort_by:
        case 'new':
            books = books.order_by('-created_at')
        case 'low_price':
            books = books.order_by('credit')
        case 'high_price':
            books = books.order_by('-credit')
        case 'bestseller':
            ...
        case 'view':
            ...


    #┌──────────────────────────────────────────┐
    #│                   Page                   │
    #└──────────────────────────────────────────┘
    books = books[0:idx + 6]
    

    #┌──────────────────────────────────────────┐
    #│                Serializer                │
    #└──────────────────────────────────────────┘
    books_serializer = BookSerializer(books, many=True)
 

    #┌──────────────────────────────────────────┐
    #│               Json-Response              │
    #└──────────────────────────────────────────┘
    return JsonResponse(books_serializer.data, safe=False)


@api_view(['POST'])
@permission_classes([])
def book_detail(request, id):
    book = Book.objects.get(pk=id)
    tags = Tag.objects.filter(books=book)
    genres = Genre.objects.filter(books=book)
    

    querySet = reduce(lambda a, b: a | b, [
        Q(genres=genre)
        for genre in genres
    ])

    if len(tags) > 0 :
        querySet = reduce(lambda a, b: a | b, [
            Q(tags=tag)
            for tag in tags
        ]) | querySet

    books = Book.objects.filter(querySet).exclude(id=id).distinct()[:request.data.get('book_index') + 6]


    book_serializer = BookDetailSerializer(book)
    books_serializer = BookSerializer(books, read_only=True, many=True)


    return JsonResponse({
        'book': book_serializer.data,
        'books': books_serializer.data,
    }, safe=False)
    
