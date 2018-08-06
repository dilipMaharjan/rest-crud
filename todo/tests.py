from django.test import TestCase


# Create your tests here.

class TestCiExample(TestCase):
    def test_true(self):
        self.assertTrue(4, 2 + 3)
