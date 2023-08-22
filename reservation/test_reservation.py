from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Reservation
from .forms import ReservationForm

class ReservationTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.reservation = Reservation.objects.create(user=self.user, date="2023-08-10", time="18:00", guests=4)

    def test_reservation_creation(self):
        reservation = self.reservation
        self.assertEqual(str(reservation), "testuser - 2023-08-10 18:00:00 - 4")

    def test_reservations_view(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse('reservation:reservations_view'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "2023-08-10")
        self.assertTemplateUsed(response, 'reservations.html')

    def test_make_reservation(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.post(reverse('reservation:make_reservation'), data={
            'date': '2023-08-20',
            'time': '19:00',
            'guests': 3,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Reservation.objects.count(), 2)

class ReservationFormTests(TestCase):
    def test_reservation_form_valid(self):
        form = ReservationForm(data={
            'date': '2023-08-20',
            'time': '19:00',
            'guests': 3,
        })
        self.assertTrue(form.is_valid())

    def test_reservation_form_invalid(self):
        form = ReservationForm(data={})
        self.assertFalse(form.is_valid())
