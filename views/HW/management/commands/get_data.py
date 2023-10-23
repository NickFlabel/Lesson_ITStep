from django.core.management import BaseCommand
from ...models import Student, Course

class Command(BaseCommand):

    def handle(self, *args, **options):
        courses = Course.objects.all()
        students = Student.objects.all()

        for course in courses:
            print(course.name)
            for student in course.students.all():
                print(student.name)
            print('\n')

        for student in students:
            print(student.name)
            for course in student.course_set.all():
                print(course.name)