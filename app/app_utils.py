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
        data=''

        if not os.path.exists(file_name):
            return None

        with open(file_name, 'r', encoding='utf8') as file:
            try:
                data = json.load(file)
            except json.decoder.JSONDecodeError:
                print("Invalid JSON file '" + file_name + "'")
            # else:
            #    print("Reading file '" + file_name + "'")

        return data
        

    @staticmethod
    def write_json_file(file_name, data):
        """
        Saves the json information to a file
        Args:
            file_name: path to the file
            data: json object to upload
        """
        print("write")
        if not os.path.exists(file_name):
            return False

        with open(file_name, 'w', encoding='utf8') as file:
            try:
                json.dump(data, file_name)
                return True
            except json.decoder.JSONDecodeError:
                print("Invalid JSON file '" + file_name + "'")
                return False
            # else:
            #    print("Reading file '" + file_name + "'")
