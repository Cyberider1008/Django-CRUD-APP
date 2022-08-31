import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crud_project.settings')
django.setup()


from app1.models import Student


def create():
    # print(fake.email())
    # print(fake.country())
    # print(fake.name())
    # print(fake.zipcode())
    # print(fake.last_name())
    # print(fake.first_name())
    for i in range(50):
        s = Student(fname = fake.first_name(), lname = fake.last_name(), address= fake.country(), pincode = fake.zipcode(), email = fake.email())
        s.save()


if __name__ == '__main__':
    print("Starting club population script...")
    from faker import Faker
    fake = Faker()
    create()
    