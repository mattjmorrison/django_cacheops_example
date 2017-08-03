from django.test import TestCase
from demo.models import MyThing


class MyTests(TestCase):

    def test_x(self):
        MyThing.objects.create(description='x')
        with self.assertNumQueries(1):
            list(MyThing.objects.all())
        with self.assertNumQueries(0):
            list(MyThing.objects.all())
