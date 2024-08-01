from rest_framework import serializers

from account.serializers import UserSerializer
from .models import Book, \
                    Publishing_Company, \
                    Author, \
                    Interpreter, \
                    Subject, \
                    Genre, \
                    Achievement, \
                    Literature


class LiteratureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Literature
        fields = (
            'id',
            'name',
        )


class LiteratureDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Literature
        fields = (
            'id',
            'name',
            'description',
            'get_image',
        )


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = (
            'id',
            'name',
        ) 


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            'id',
            'name',
            'get_image',
            'readable_credit',
        )


class SubjectDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = (
            'id',
            'name',
            'description',
            'get_image',
        )


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            'id',
            'name',
            'description',
        )


class InterpreterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interpreter
        fields = (
            'id',
            'name',
        )


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = (
            'id',
            'name',
        )


class PublishingCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Publishing_Company
        fields = (
            'id',
            'name',
            'get_image',
        )


class PublisherDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publishing_Company
        fields = (
            'id',
            'name',
            'get_image',
            'description',
        )


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = (
            'id',
            'name',
        )


class ChoiceField(serializers.ChoiceField):

    def to_representation(self, obj):
        if obj == '' and self.allow_blank:
            return obj
        return self._choices[obj]

    def to_internal_value(self, data):
        # To support inserts with the value
        if data == '' and self.allow_blank:
            return ''

        for key, val in self._choices.items():
            if val == data:
                return key
        self.fail('invalid_choice', input=data)


class BookDetailSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    author = AuthorSerializer(read_only=True)
    interpreter = InterpreterSerializer(read_only=True)
    genres = GenreSerializer(read_only=True, many=True)
    subject = SubjectSerializer(read_only=True)
    publisher = PublishingCompanySerializer(read_only=True)
    achievements = AchievementSerializer(read_only=True, many=True)
    material = ChoiceField(choices=Book.MATERIAL_CHOICES)
    size = ChoiceField(choices=Book.Size.choices)

    class Meta:
        model = Book
        fields = (
            'id',
            'isbn',
            'name',
            'author',
            'interpreter',
            'genres',
            'subject',
            'publisher',
            'created_by',
            'get_image',
            'readable_credit',
            'material',
            'size',
            'pages',
            'introduction',
            'achievements',
        )
    
    def get_material(self,obj):
        return obj.get_material_display()
    
    def get_size(self,obj):
        return obj.get_size_display()