"""
    Customer information and methods
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

    def __init__(self, name=None, age=None, email=None, phone=None):
        """
        initializes and creates customer object
        args:
            name: Customer's name
            age: Customer's age
            email: Customer's email
            phone: Customer's phone numer
            empty: Track if the object is created wihtout contents
        """
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone
        if name:
            self.empty = False
        else:
            self.empty = True


    def create_customer(self, file_name="data/customers.json"):
        """
        Builds a json structure with the information and then
        saves it into the customer's json file.
        """
        new_customer = {}
        if self.empty:
            print("No Data")
        else:
            print("Create")
            new_customer = {
                'customer_name': self.name,
                'age': self.age,
                'email': self.email,
                'phone': self.phone
            }

            file_data = appUtils.read_json_file(file_name)
            if appUtils.is_customer(file_data, self.email):
                print("Customer already exists.")
            else:
                print("Adding New Customer: " + self.email)
                appUtils.write_json_file(new_customer, file_name)


    def delete_customer():
        print("delete")


    def display_customer_information(self, email=None, file_name="data/customers.json"):
        """
        Shows the customer's information, if exists, to the console
        Args:
            email: the identification to search the customer
            file_name: location of the customer's information
        """
        print("Customer Information:")

        if email == None:
            customer_email = self.email
        else:
            customer_email = email

        file_data = appUtils.read_json_file(file_name)
        customer_info = None

        if file_data is not None:
            for customer in file_data:
                if customer_email == customer.get('email'):
                    customer_info = customer

            if customer_info is not None:
                # print(customer_info)
                print("Name: " + customer_info.get('customer_name')
                    + "\nAge: " + str(customer_info.get('age'))
                    + "\nEmail: " + customer_info.get('email')
                    + "\nPhone: " + customer_info.get('phone'))
            else:
                print("Customer with email '" + customer_email + "' Not Found!")


    def modify_customer_information(customer_name):
        """
        Updates or modifies customer information, if exists
        Args:
            customer_name: the desired customer name to update
        """
        print("modify")
