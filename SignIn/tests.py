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
                                             email="john.doe@generic.com",
                                             major='CSCI', dob='2000-01-01',
                                             academicYear='FR')

    def test_school_id_taken(self):
        # Issue a GET request.
        response = self.client.get('/school_id_taken', data={'schoolId': 'Y00123456'})

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains 5 customers.
        self.assertTrue(response.json()['isTaken'])

    def test_create_student_valid(self):
        response = self.client.post('/create_student', data={'schoolId': 'Y00000000',
                                                             'firstName': 'Boobs',
                                                             'lastName': 'McGee',
                                                             'sex': 'F',
                                                             'email': 'boobs.mcgee@merica.edu',
                                                             'dob': '1998-05-25',
                                                             'major': 'CSCI',
                                                             'academicYear': 'FR'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()['student_is_valid'])

    def test_create_student_invalid_id(self):
        response = self.client.post('/create_student', data={'schoolId': '000000000',
                                                             'firstName': 'Boobs',
                                                             'lastName': 'McGee',
                                                             'sex': 'F',
                                                             'email': 'boobs.mcgee@merica.edu',
                                                             'dob': '1998-05-25',
                                                             'major': 'CSCI',
                                                             'academicYear': 'FR'})
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.json()['student_is_valid'])


