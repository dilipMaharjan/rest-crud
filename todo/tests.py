from django.test import TestCase


# Create your tests here.

class TestCiExample(TestCase):
    def test_equal(self):
        self.assertEqual("hello", "hello")

    def test_false(self):
        self.assertFalse(False)

    def test_true(self):
        self.assertTrue(False)
