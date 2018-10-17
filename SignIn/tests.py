from django.test import TestCase
from django.test import Client
from SignIn.models import Student

# Create your tests here.
class ViewsTests(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    @classmethod
    def setUpTestData(cls):
        cls.student = Student.objects.create(schoolId="Y00123456", firstName="John",
                                             lastName="Doe", sex="M",
                                             email="john.doe@generic.com")

    def test_school_id_taken(self):
        # Issue a GET request.
        response = self.client.get('/school_id_taken', data={'schoolId': 'Y00123456'})

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains 5 customers.
        self.assertTrue(response.json()['isTaken'])