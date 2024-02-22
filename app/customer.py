"""
Customer Class
Contains methods and variables to manage Customer objects
"""

from app.app_utils import appUtils


class Customer:
    """
    Class to represent a Customer in the Hotel app

    Variables:
        name: Customer's name
        age: Customer's age
        email: Customer's email
        phone: Customer's phone number
    """

    file_name = "data/customers.json"

    def __init__(self, email=None, name="", age=0, phone=""):
        """
        initializes and creates a CUSTOMER object
        args:
            name: Customer's name
            age: Customer's age
            email: Customer's email
            phone: Customer's phone numer
        """
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone

        # empty: to track if the object is created wihtout parameters
        if email:
            self.empty = False
        else:
            self.empty = True

    def create_customer(self):
        """
        Builds a json structure with the info from the object and then
        saves it into the customer's json file.
        """
        new_customer = {}
        if self.empty:
            print("No Data found to create a Customer.")
        else:
            # print("Create")
            new_customer = {
                'customer_name': self.name,
                'age': self.age,
                'email': self.email,
                'phone': self.phone
            }

            file_data = appUtils.read_json_file(self.file_name)
            if appUtils.is_customer(file_data, self.email):
                print("Customer already exists.")
            else:
                print("Adding New Customer: " + self.email)
                appUtils.write_new_entry_json_file(
                                    new_customer, self.file_name)

    def delete_customer(self):
        """
        Removes a customer from the file of customers
        """

        if self.empty:
            print("Nothing to delete")
        else:
            print("Deleting Customer: " + self.email)

            file_data = appUtils.read_json_file(self.file_name)

            if file_data is not None:
                remaining_customers = [
                    customer for customer in file_data
                    if customer['email'] != self.email
                ]
                appUtils.write_to_json_file(
                                    remaining_customers, self.file_name)
                self.clear_data()

    def display_customer_information(self):
        """
        Shows the customer's information, if exists, to the console
        Args:

        """
        if self.empty:
            print("No customer information available")
        else:
            print(">> Customer Information:")
            print("Name: " + self.name
                  + "\nAge: " + str(self.age)
                  + "\nEmail: " + self.email
                  + "\nPhone: " + self.phone
                  + "\n")

    def modify_customer_information(self, email=None, name=None,
                                    age=None, phone=None):
        """
        Updates or modifies customer information, if exists
        Args:
            name: the new customer name to update
        """
        print("Modifying Customer information")

        if self.empty:
            print("Nothing to update. Please, load a customer")
        else:   # there's data in the object, so...
            # serach for the customer to update
            file_data = appUtils.read_json_file(self.file_name)
            if file_data is not None:
                for customer in file_data:
                    if customer['email'] == self.email:
                        new_data = {
                            'email': self.email,
                            'customer_name': name,
                            'age': age,
                            'phone': phone
                        }
                        customer.update(new_data)
                        break
                appUtils.write_to_json_file(file_data, self.file_name)
                print("Customer information updated.")
            else:
                print("Nothing to update.")

    def get_customer_information(self, email=None):
        """
        Searches for a customer in the Customer file,
        the information can be used to be displayed or updated
        """
        print("getting Customer Information...")

        if email is None:
            customer_email = self.email
        else:
            customer_email = email

        file_data = appUtils.read_json_file(self.file_name)
        customer_info = None

        if file_data is None:
            print("Not able to read Customer json file...")
        else:
            for customer in file_data:
                if customer_email == customer.get('email'):
                    customer_info = customer

            if customer_info is None:
                print("Customer with email '" + customer_email
                      + "' Not Found at the JSON File!")
            else:
                # save customer into local variables
                self.name = customer_info.get('customer_name')
                self.age = customer_info.get('age')
                self.email = customer_info.get('email')
                self.phone = customer_info.get('phone')
                self.empty = False

    def clear_data(self):
        """
        clears the object data.
        To do a clean search or when removing a customer from the file
        """
        self.name = None
        self.age = 0
        self.email = None
        self.phone = None
        # empty: to track if the object is created wihtout parameters
        self.empty = True
