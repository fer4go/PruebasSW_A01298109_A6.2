"""
Unit tests for hotel class
"""
import unittest
import json
import sys
sys.path.insert(0, '../PruebasSW_A01298109_A6.2')
from app.hotel import Hotel
from app.app_utils import appUtils


class TestHotelClass(unittest.TestCase):
    """
    Test class for Hotel
    """

    def setUp(self):
        print("setup...")
        Hotel.file_name = "test_data/test_hotels.json"

        self.hotel1 = Hotel(
                    "Test Hotel", "Downtown", "All Inclusive", 5)

    def test_a_create_first_hotel(self):
        print("> test_create_first_hotel.")
        # to clean the test_customers.json file
        json_var = json.loads('[]')
        appUtils.write_to_json_file(json_var, Hotel.file_name)

        self.hotel1.create_hotel()

        hotels = appUtils.read_json_file(Hotel.file_name)

        self.assertIsNotNone(hotels)
        self.assertEqual(len(hotels), 1)
        self.assertEqual(hotels[0]['hotel_name'], "Test Hotel")
        self.assertEqual(hotels[0]['location'], "Downtown")
        self.assertEqual(len(hotels[0]['rooms']), 5)

    def test_b_modify_hotel_information(self):
        print("> test_modify_hotel_information")


        self.hotel1.modify_hotel_information(
                    "Test Data", "City", "All Inclusive", 3)

        hotels = appUtils.read_json_file(Hotel.file_name)

        self.assertIsNotNone(hotels)
        self.assertEqual(len(hotels), 1)
        self.assertEqual(hotels[0]['location'], "City")
        self.assertEqual(len(hotels[0]['rooms']), 3)

    #def test_c_delete_hotel(self):
    #    print("> test_delete_hotel")
    #    self.hotel1.delete_hotel()

    #    hotels = appUtils.read_json_file(Hotel.file_name)

    #    self.assertIsNotNone(hotels)
    #    self.assertEqual(len(hotels), 0)

if __name__ == '__main__':
    unittest.TestLoader.sortTestMethodsUsing = None
    # sortTestMethodsUsing = lambda *args: -1
    unittest.main()
