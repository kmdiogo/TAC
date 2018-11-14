from django.test import TestCase
from django.test import Client
from rest_framework.test import APIClient
from SignIn.models import Student, Session
from Dashboard.models import *
from django.contrib.auth.models import User
from django.test.utils import override_settings


# Create your tests here.
class ViewsTests(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = APIClient()

    @classmethod
    def setUpTestData(cls):
        cls.student = Student.objects.create(schoolId="Y00123456", firstName="John",
                                             lastName="Doe", sex="M",
                                             email="john.doe@generic.com",
                                             dob="1980-04-05")
        cls.employeeUser = User.objects.create(username="Y00123456")

        cls.session = Session.objects.create(student=cls.student, course="MATH 1510", reason="test review")

    def test_student_retrieve_valid(self):
        response = self.client.get('/tac-api/students/Y00123456', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_student_retrieve_invalid(self):
        response = self.client.get('/tac-api/students/Y00654321', follow=True)
        self.assertEqual(response.status_code, 404)

    def test_open_session_retrieve_valid(self):
        response = self.client.get('/tac-api/sessions/Y00123456', follow=True)
        self.assertEqual(response.status_code, 200)


    def test_clock_in_shift_non_existent_employee(self):
        response = self.client.post('/tac-api/shifts/clockin/Y00654321', follow=True)
        self.assertEqual(response.status_code, 404)

    def test_clock_in_shift(self):
        response = self.client.post('/tac-api/shifts/clockin/Y00123456', follow=True)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Shift.objects.filter(user__username__iexact='Y00123456'))

    def test_clock_in_shift_bad_response(self):
        response = self.client.post('/tac-api/shifts/clockin/Y00123456', follow=True)
        response = self.client.post('/tac-api/shifts/clockin/Y00123456', follow=True)
        self.assertEqual(response.status_code, 400)

    #@override_settings(DEBUG=True)
    def test_clock_out_session_retrieve_valid(self):
        response = self.client.post('/tac-api/shifts/clockin/Y00123456', follow=True)
        response = self.client.put('/tac-api/shifts/clockout/Y00123456', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_clock_out_session_retrieve_invalid404(self):
        response = self.client.post('/tac-api/shifts/clockin/Y00123456', follow=True)
        response = self.client.put('/tac-api/shifts/clockout/shit', follow=True)
        self.assertEqual(response.status_code, 404)

    def test_clock_out_session_retrieve_invalid400(self):
        response = self.client.put('/tac-api/shifts/clockout/shit', follow=True)
        self.assertEqual(response.status_code, 404)


    # def test_school_id_taken(self):
    #     # Issue a GET request.
    #     response = self.client.get('/school_id_taken', data={'schoolId': 'Y00123456'})
    #
    #     # Check that the response is 200 OK.
    #     self.assertEqual(response.status_code, 200)
    #
    #     # Check that the rendered context contains 5 customers.
    #     self.assertTrue(response.json()['isTaken'])
    #
    #     #test to check that that form is filled with valid entries
    # def test_create_student_valid(self):
    #     response = self.client.post('/create_student', data={'schoolId' : 'Y00000000',
    #                                                          'firstName' : 'Boobs',
    #                                                          'lastName': 'McGee',
    #                                                          'sex' : 'F',
    #                                                          'email': 'boobs.mcgee@merica.edu'})
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTrue(response.json() ['student_is_valid'])

