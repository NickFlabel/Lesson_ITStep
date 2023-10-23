from django.core.management import BaseCommand
from ...models import Student, Course

class Command(BaseCommand):

    def handle(self, *args, **options):
        student1 = Student.objects.create(name='test1')
        student2 = Student(name='test2')
        student2.save()
        student3 = Student.objects.create(name='test3')

        course1 = Course.objects.create(name='test_c1')
        course2 = Course.objects.create(name='test_c2')
        course3 = Course.objects.create(name='test_c3')
        course3.students.set([student1, student2])