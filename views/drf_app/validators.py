from rest_framework import serializers


def number_of_letters_validator(value):
    if len(value) < 3:
        raise serializers.ValidationError('Длина имени должна быть больше трех символов')
    return value
