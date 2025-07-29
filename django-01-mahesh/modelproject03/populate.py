import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'modelproject03.settings')
django.setup()

from faker import Faker
from testapp.models import Student
from random import *

def mobileNumberGenerator():
    d1 = randint(6,9)
    num = str(d1)
    for i in range(9):
        num  = num + str(randint(0,9))
    return int(num)

def populate(n):
    fake = Faker()
    for i in range(n):
        fSId = fake.random_int(min=200004001, max=200006000)
        fSName = fake.name()
        fSEmail = str(fSId) + '@kluniversity.in'
        fSMobileNo = mobileNumberGenerator()
        fSMarks = fake.random_int(min=0, max=100)
        fSAddress = fake.address()
        Student.objects.get_or_create(sId=fSId, sName=fSName, sEmail=fSEmail, sMobileNo=fSMobileNo,sMarks=fSMarks,sAddress=fSAddress)


n = int(input('Enter no of student: '))
populate(n)
print(f'{n} records are successfully inserted.')


