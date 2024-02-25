"""
Unit tests for customer class
"""
from app.customer import Customer
from app.app_utils import appUtils

import unittest
import json
import sys
sys.path.insert(0, '../PruebasSW_A01298109_A6.2')


class TestCustomerClass(unittest.TestCase):
    """
    Test class for Customer
    """

    def setUp(self):
        Customer.file_name = "test_data/test_customers.json"

        self.customer1 = Customer(
                          "jane@mail.com", "Jane Doe", 27, "987-654-321")
        self.customer2 = Customer(
                          "joe@mail.com", "Joe Doe", 29, "654-321-987")

    def test_create_first_customer(self):
        print("> test_create_first_customer.")
        # to clean the test_customers.json file
        json_var = json.loads('[]')
        appUtils.write_to_json_file(json_var, Customer.file_name)
        # 1st customer:
        self.customer1.create_customer()

        customers = appUtils.read_json_file(Customer.file_name)

        self.assertIsNotNone(customers)
        self.assertEqual(len(customers), 1)
        self.assertEqual(customers[0]['customer_name'], "Jane Doe")

    def test_create_second_customer(self):
        print("> test_create_second_customer.")
        self.customer2.create_customer()

        customers = appUtils.read_json_file(Customer.file_name)

        self.assertIsNotNone(customers)
        self.assertEqual(len(customers), 2)
        self.assertEqual(customers[1]['customer_name'], "Joe Doe")

    def test_get_cutomer_information(self):
        print("> test_get_cutomer_information.")
        self.customer1.get_customer_information("jane@mail.com")
        self.assertEqual(self.customer1.name, "Jane Doe")

    def test_delete_customer(self):
        print("> test_delete_customer.")
        self.customer1.get_customer_information("joe@mail.com")
        self.customer1.delete_customer()

        customers = appUtils.read_json_file(Customer.file_name)

        self.assertIsNotNone(customers)
        self.assertEqual(len(customers), 1)

    def test_modify_customer_information(self):
        print("> test_modify_customer_information.")
        self.customer1.get_customer_information("jane@mail.com")
        self.customer1.modify_customer_information(
                    "jane@mail.com", "Juana Does", 27, "987-654-321")

        customers = appUtils.read_json_file(Customer.file_name)

        self.assertIsNotNone(customers)
        self.assertEqual(len(customers), 1)
        self.assertEqual(customers[0]['customer_name'], "Juana Does")

    def test_clear_data(self):
        print("> test_clear_data.")
        self.customer2.clear_data()

        self.assertIsNone(self.customer2.name)

if __name__ == '__main__':
    unittest.main()
