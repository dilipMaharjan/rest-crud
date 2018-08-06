from django.test import TestCase


# Create your tests here.

class TestCiExample(TestCase):
    def test_true(self):
        self.assertEqual("hello", "not equal")
