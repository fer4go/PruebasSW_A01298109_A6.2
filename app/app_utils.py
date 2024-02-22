"""
Utils support methods
"""

import os
import json


class appUtils:

    @staticmethod
    def read_json_file(file_name):
        """
        Reads a json file with the app information:
            - customers
            - hotel
            - reservation
        Args:
            file_name: path to the JSON file
            return json structure
        """
        file_data=''

        if not os.path.exists(file_name):
            print("File '" + file_name + "' not found.")
            return None

        with open(file_name, 'r', encoding='utf8') as file:
            try:
                file_data = json.load(file)
            except json.decoder.JSONDecodeError:
                print("Invalid JSON file '" + file_name + "'")
            # else:
            #    print("Reading file '" + file_name + "'")
        return file_data

    @staticmethod
    def write_new_entry_json_file(new_entry, file_name):
        """
        Saves new record into the json file
        Args:
            new_entry: part of the json to be append
            file_name: path to the file
        """
        print("saving...")
        if not os.path.exists(file_name):
            return False

        with open(file_name, 'r+', encoding='utf8') as file:
            try:
                # load existing data
                file_data = json.load(file)
                # join new data
                file_data.append(new_entry)
                # set file position at offset
                file.seek(0)
                # convert to json
                json.dump(file_data, file)
            except json.decoder.JSONDecodeError:
                print("Invalid JSON file '" + file_name + "'")

    @staticmethod
    def write_to_json_file(data, file_name):
        """
        Saves new record into the json file
        Args:
            data: the json to be saved
            file_name: path to the file
        """
        print("saving...")
        if not os.path.exists(file_name):
            return False

        with open(file_name, 'w', encoding='utf8') as jsonfile:
            try:
                # convert to json
                json.dump(data, jsonfile)
            except json.decoder.JSONDecodeError:
                print("Invalid JSON file '" + file_name + "'")

    @staticmethod
    def is_customer(file_data, customer_email):
        """
        validate if the customer exists in the customers json file
        """
        customer_flag = False
        if file_data is not None:
            for customer in file_data:
                if customer_email == customer.get('email'):
                    customer_flag = True
                    break
        return customer_flag

    @staticmethod
    def is_hotel(file_data, hotel_name):
        """
        validate if the hotel exists in the hotels json file
        """
        hotel_flag = False
        if file_data is not None:
            for hotel in file_data:
                if hotel_name == hotel.get('hotel_name'):
                    hotel_flag = True
                    break
        return hotel_flag

    @staticmethod
    def is_reservation(file_data, hotel, customer, room_number):
        """
        validate if the reservation exists in the reservation json file
        """
        reservation_flag = True
        if file_data is not None:
            for reservation in file_data:
                print(reservation.get('hotel_name'))
                #if hotel == reservation.get('hotel_name')
                    #    and customer == reservation.get('customer')
                    #    and room_number == reservation.get('room_number')
                #    reservation_flag = True
                #    break
        return reservation_flag
