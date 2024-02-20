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

        customer_flag = False
        if file_data is not None:
            for customer in file_data:
                if customer_email == customer.get('email'):
                    customer_flag = True

        return customer_flag
