"""
Reservation class
Contains the methods and variables to manage Reservation objects
"""

#from app.hotel import Hotel
#from app.customer import Customer
from app.app_utils import appUtils


class Reservation:
    """
    Class to represent the Hotel Reservations.
    """

    file_reservation = "data/reservations.json"
    file_customer = "data/customers.json"
    file_hotel = "data/hotels.json"

    def __init__(self, hotel_name=None, customer_email=None, room_number=0):
        """
        initializes and creates a RESERVATION object
        args:
            hotel_name: Hotel's name
            customer_email: customer's email
            room_number: number of rooms at the hotel
            type: Hotel's room type
        """
        print("reservation object")
        self.hotel = hotel_name
        self.customer_email = customer_email
        self.room_number = room_number

    def create_reservation(self):
        """
        Creates a reservation for the Hotel app
        Args:
            customer(string): customer name
            hotel(string): hotel name
            room_number(number): a valid number of the hotel
        """
        print("Creating a Reservation")
        file_res_data = appUtils.read_json_file(self.file_reservation)

        if appUtils.is_reservation(file_res_data,
                        self.hotel, self.customer_email, self.room_number):
            print("Reservation already exists.")
        else:
            customers_data = appUtils.read_json_file(self.file_customer)
            hotels_data = appUtils.read_json_file(self.file_hotel)

            if appUtils.is_customer(customers_data, self.customer_email):
                    #and appUtils.is_hotel(hotels_data, self.hotel_name):
                print("Adding New Reservation: ")
                #appUtils.write_new_entry_json_file(
                #                new_customer, self.file_name)
            else:
                print("Customer name or Hotel name are invalid")

    def cancel_reservation(hotel, customer, room_number):
        """
        Removes a reservation for the Hotel app
        Args:
            customer(string): customer name
            hotel(string): hotel name
            room_number(number): a valid number of the hotel
        """
        print("hello")
