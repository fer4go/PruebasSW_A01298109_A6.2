"""
Hotel class
Contains the methods and variables to manage Hotel objects
"""

from app.app_utils import appUtils

class Hotel:
    """
    Class to represent a Hotel in the Hotel app
    Variables:
        name (str): hotel name
        location (str): city where location is located
        rooms_qty: quantity of rooms in the hotel
        type (str): room type
        rooms (list): list of rooms and their characteristics
    """

    file_name = "data/hotels.json"

    def __init__(self, name=None, location=None, rooms_qty=0, type=None):
        """
        initializes and creates a HOTEL object
        args:
            name: Hotel's name
            location: Hotel's city location
            room_qty: number of rooms at the hotel
            type: Hotel's room type
        """
        self.hotel_name = name
        self.location = location
        self.rooms_qty = rooms_qty
        self.type = type

        list = []
        for i in range(rooms_qty):
            list.append({"room":i+101, "reserved": "No"})

        self.rooms = list

        # to track if the object is created without parameters
        if name:
            self.empty = False
        else:
            self.empty = True


    def create_hotel(self):
        """
        Builds json structure with the hotel information, then
        inserts a hotel to the json file
        """
        new_hotel = {}
        if self.empty:
            print("No Data found to create a Hotel")
        else:
            print("Creating a Hotel: " + self.hotel_name)
            new_hotel = {
                "hotel_name": self.hotel_name,
                "location": self.location,
                "rooms_qty": self.rooms_qty,
                "type": self.type,
                "rooms": self.rooms
            }

            file_data = appUtils.read_json_file(self.file_name)
            if appUtils.is_hotel(file_data, self.hotel_name):
                print("Hotel already exists.")
            else:
                print("Adding new Hotel: " + self.hotel_name)
                print(new_hotel)
                appUtils.write_new_entry_json_file(new_hotel, self.file_name)


    def display_hotel_information(self):
        """
        prints the hotel information loaded in the object to the user
        """
        if self.empty:
            print("No Hotel information available to display")
        else:
            print(">> Hotel Information:")
            print("Name: " + self.hotel_name
                + "\nLocation: " + self.location
                + "\nNumber of Rooms: " + str(self.rooms_qty)
                + "\nHotel Type: " + self.type
                + "\nRooms: "
            )
            for room in self.rooms:
                print("\tRoom: " + str(room['room'])
                    + " - Reserved: " + room['reserved'])


    def delete_hotel(self):
        """
        removes a hotel from the list of hotels
        """
        if self.empty:
            print("Nothing to delete")
        else:
            print("Deleting Hotel: "+ self.hotel_name)

            file_data = appUtils.read_json_file(self.file_name)
            if file_data is not None:
                remaning_hotels = [
                    hotel for hotel in file_data
                    if hotel['hotel_name'] != self.hotel_name
                ]
                appUtils.write_to_json_file(remaning_hotels, self.file_name)
                self.clear_data()


    def modify_hotel_information(self, name=None, location=None, type=None,
                                rooms_qty=0):
        """
        upates the hotel information
        """
        print("Modifying Hotel Information")
        if self.empty:
            print("Nothing to update. Please, load a Hotel")
        else:
            # search for the customer object ot update
            file_data = appUtils.read_json_file(self.file_name)
            if file_data is not None:
                for hotel in file_data:
                    if hotel['hotel_name'] == self.hotel_name:
                        #room_list = hotel['rooms']
                        self.location = location
                        self.rooms_qty = rooms_qty
                        self.type = type
                        new_data = {
                            'hotel_name': self.hotel_name,
                            'location': location,
                            'rooms_qty': rooms_qty,
                            'type': type,
                            "rooms": self.rooms
                        }
                        hotel.update(new_data)
                        break

                appUtils.write_to_json_file(file_data, self.file_name)
                print("Hotel information updated.")
            else:
                print("Nothing to update.")


    def get_hotel_information(self, name=None):
        """
        searches for a hotel from the Hotel json file
        """
        print("getting Hotel information...")
        if name == None:
            hotel_name = self.hotel_name
        else:
            hotel_name = name

        file_data = appUtils.read_json_file(self.file_name)
        hotel_info = None

        if file_data is not None:
            for hotel in file_data:
                if hotel_name == hotel.get('hotel_name'):
                    hotel_info = hotel

            if hotel_info is not None:
                self.hotel_name = hotel_info.get('hotel_name')
                self.location = hotel_info.get('location')
                self.room_qty = hotel_info.get('room_qty')
                self.type = hotel_info.get('type')
                self.rooms = hotel_info.get('rooms')
                self.empty = False
            else:
                print("Hotel with name '" + hotel_name
                    + "' Not Found at the JSON File!")


    def reserve_a_room(self, hotelName):
        """
        makes a reservation to a room within a hotel
        """

    def cancel_a_reservation(self, hotelName):
        """
        removes the reservation of a room in a hotel
        """

    def clear_data(self):
        """
        clears the object data
        """
        self.hotel_name = None
        self.location = None
        self.room_qty = 0
        self.type = None
        self.rooms = []
        self.empty = True
