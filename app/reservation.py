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
            room_number: number of the room at the hotel
        """
        # print("reservation object")
        self.hotel_name = hotel_name
        self.cust_email = customer_email
        self.room_number = room_number

        # empty: to track if the object is created wihtout parameters
        if hotel_name:
            self.empty = False
        else:
            self.empty = True

    def show_all_reservations(self, file_data):
        for reservation in file_data:
            print("Hotel: " + reservation['hotel_name']
                  + "\nCustomer: " + reservation['customer_email']
                  + "\nRoom Number: " + reservation['room_number'])

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
                        self.hotel_name, self.cust_email, self.room_number):
            print("Reservation already exists.")
        else:
            customers_data = appUtils.read_json_file(self.file_customer)
            hotels_data = appUtils.read_json_file(self.file_hotel)
            print(customers_data)
            print(hotels_data)
            if (appUtils.is_customer(customers_data, self.cust_email)
                 and appUtils.is_hotel(hotels_data, self.hotel_name)
            ):
                print("Adding New Reservation: ")
                new_reservation = {
                    'hotel_name': self.hotel_name,
                    'customer_email': self.cust_email,
                    'room': self.room_number
                }
                appUtils.write_new_entry_json_file(
                                new_reservation, self.file_reservation)
            else:
                print("Customer name or Hotel name are invalid")

    def cancel_reservation(self):
        """
        Removes a reservation for the Hotel app
        Args:
            customer(string): customer name
            hotel(string): hotel name
            room_number(number): a valid number of the hotel
        """
        print("Removing Reservation")
        if self.empty:
            print("No reservation to remove")
        else:
            file_data = appUtils.read_json_file(self.file_reservation)

            if file_data is not None:
                if appUtils.is_reservation(file_data,
                            self.hotel_name, self.cust_email, self.room_number):
                    print("Reservation exists.")
                    print("removing...")
                    remaining_reservation = [
                        reservation for reservation in file_data
                        if (#reservation['hotel_name'] != self.hotel_name
                            reservation['customer_email'] != self.cust_email
                            and reservation['room_number'] != self.room_number
                        )
                    ]
                    #appUtils.write_to_json_file(
                    #                remaining_reservation,
                    #                self.file_reservation
                    #)
                    #self.clear_data()
                    for res in remaining_reservation:
                        print("Hotel: " + res['hotel_name'])

                else:
                    print("Reservation does not exist.")
                    #show_all_reservations(file_data)
            else:
                print("File does not exist.")


    def clear_data(self):
        """
        clears the object data.
        To do a clean search or when removing a customer from the file
        """
        self.hotel_name = None
        self.cust_email = None
        self.room_number = 0
        # empty: to track if the object is created wihtout parameters
        self.empty = True
