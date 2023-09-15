from django import forms
from .models import Author, Post, Category
from django.forms import modelform_factory, modelformset_factory
from django import forms
from django.contrib.auth.models import User

from captcha.fields import CaptchaField


class CaptchaForm(forms.ModelForm):

    # captcha = CaptchaField()

    class Meta:
        model = Category
        fields = '__all__'


author_form = modelform_factory(Author, fields='__all__') # -> class
# первый аргумент - модель
# fields/exclude - ['name', 'email']
# exclude - ['bio']


class PostForm(forms.ModelForm):

    class Meta:
        # обязательные
        model = Post
        fields = '__all__'
        # exclude = ['views']
        # опциональное
        labes = {'title': 'Название поста', 'content': 'Содержание поста'}
        help_text = {'title': 'Введите название поста'}
        widgets = {'authors': forms.widgets.Select(attrs={'size': 2})}


class PostFormAlt(forms.ModelForm):

    title = forms.CharField(label='Название поста')
    content = forms.CharField(label='Содержание поста', widget=forms.widgets.Textarea())
    author = forms.ModelChoiceField(queryset=Author.objects.all(), label='Автор', help_text='Выберите категории',
                                    widget=forms.widgets.Select(attrs={'size': 2})) # <select size=2></select>
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), label='Категории',
                                                widget=forms.widgets.SelectMultiple(attrs={'size': 4}))

    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'categories', 'views', 'status']


class UserRegistrationForm(forms.ModelForm):

    password1 = forms.CharField(label='Пароль', widget=forms.widgets.PasswordInput())
    password2 = forms.CharField(label='Пароль (поторно)', initial='1234')
    my_site = forms.URLField(min_length=1, max_length=100, required=False)
    regex_field = forms.RegexField('^[a-zA-Z]{4}$', widget=forms.widgets.TextInput())
    is_client = forms.BooleanField()
    decided_to_join = forms.NullBooleanField()
    number_of_goods = forms.IntegerField()
    rate = forms.FloatField()
    balance = forms.DecimalField(max_digits=10, decimal_places=2)
    choice = forms.ChoiceField(choices=(('f', 'first'), ('s', 'second')))
    choice2 = forms.MultipleChoiceField(choices=(('f', 'first'), ('s', 'second')))
    # label: str, который будет отображаться в html-форме
    # help_text: str, который будет отображаться рядом с полем
    # initial: Any значение: которое будет вводится в форму по умолчанию
    # required: bool True
    # widget: Any класс: который мы передаем дял того чтого указать django, какой html-таг использовтаь
    # при рендеринге страницы
    # validator: list

    # HTML-tags
    # forms.widgets
    # Textinput - большое текстовое поле
    # NumberInput - <input type=number>
    # urlinput
    # PasswordInput
    # Dateinput

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class SimpleForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'


class AuthorSearchForm(forms.Form):
    author_name = forms.CharField(max_length=100, label='Имя автора')


Formset = modelformset_factory(Author, fields='__all__')
