from rest_framework import serializers
from .models import Author, Location, Publisher, Book
from .validators import number_of_letters_validator
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator

from django.shortcuts import get_object_or_404


class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100, validators=[number_of_letters_validator])
    birthdate = serializers.DateField()

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.birthdate = validated_data.get('birthdate', instance.birthdate)
        instance.save()
        return instance

    def create(self, validated_data):
        return Author.objects.create(**validated_data)

    class Meta:
        validators = [
            UniqueTogetherValidator(
                queryset=Author.objects.all(),
                fields=['name', 'birthdate']
            )
        ]

    #
    # def validate(self, attrs):
    #     if str(attrs['birthdate']) > '2020-01-01':
    #         raise serializers.ValidationError('Дата рождения должна быть раньше, чем 2020-01-01')
    #     if len(attrs['name']) < 3:
    #         raise serializers.ValidationError("Длина имени должна быть больше трех символов")
    #     return attrs


class AuthorUpdateSerializer(AuthorSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100, required=False)
    birthdate = serializers.DateField(required=False)


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = '__all__'


class PublisherSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[number_of_letters_validator,
                                             UniqueValidator(queryset=Publisher.objects.all())])
    location = LocationSerializer()

    class Meta:
        model = Publisher
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    # {"title": "test", "pub_date": "2020-01-01", "authors": [{"name": "author_1", "birthdate": "2000-01-01"},
    # {"name": "author_2", "birthdate": "1999-01-01"}], "publisher": {"name": "test", "location":
    # {"name": "loc"}}}

    class Meta:
        model = Book
        fields = '__all__'




