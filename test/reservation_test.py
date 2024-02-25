"""
Unit tests for reservation class
"""
import unittest
import json
import sys
sys.path.insert(0, '../PruebasSW_A01298109_A6.2')
from app.customer import Customer
from app.hotel import Hotel
from app.reservation import Reservation
from app.app_utils import appUtils


class TestReservationClass(unittest.TestCase):
    """
    Test class for Reservation
    """

    def setUp(self):

        Reservation.file_reservation = "test_data/test_reservations.json"
        Reservation.file_customer = "test_data/test_customers.json"
        Reservation.file_hotel = "test_data/test_hotels.json"

        Customer.file_name = "test_data/test_customers.json"
        Hotel.file_name = "test_data/test_hotels.json"

        self.hotel = Hotel(
                        "Test Hotel", "Downtown", "All Inclusive", 5)
        self.customer = Customer(
                        "jane@mail.com", "Jane Doe", 27, "987-654-321")
        self.reservation = Reservation("Test Hotel", "jane@mail.com", 101)

        self.hotel.create_hotel()
        self.customer.create_customer()

    def test_a_create_reservation(self):
        print("> test_create_reservation.")
        # to clean the test_reservations.json file
        json_var = json.loads('[]')
        appUtils.write_to_json_file(json_var, Reservation.file_reservation)

        self.reservation.create_reservation()

        reservations = appUtils.read_json_file(Reservation.file_reservation)

        self.assertIsNotNone(reservations)
        self.assertEqual(len(reservations), 1)
        self.assertEqual(reservations[0]['hotel_name'], "Test Hotel")
        self.assertEqual(reservations[0]['room'], 101)

if __name__ == '__main__':
    unittest.main()
