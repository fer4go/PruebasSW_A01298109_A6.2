"""
"""
from app.hotel import Hotel
from app.customer import Customer
from app.reservation import Reservation


def main():
    """
    main test function
    """
    print("main")
    #Customer.display_customer_information("Customer Name1")
    customer = Customer("hp@mail.com","HP",46,"321-123-456")
    #customer.get_customer_information()
    #customer.create_customer()
    customer.display_customer_information()
    #customer.get_customer_information()
    #customer.display_customer_information()
    #customer.create_customer()

    #customer2 = Customer()
    #customer2.display_customer_information()
    #customer2.get_customer_information("arthur.doyle@mail.com")
    #customer2.display_customer_information()
    #customer2.modify_customer_information("arthur.doyle@mail.com",
    #                        "Arthur Conan Doyle",
    #                        71, "123-456-7890")
    #customer2.display_customer_information()

    customer.delete_customer()
    #customer2.get_customer_information("hp@mail.com")
    customer.display_customer_information()


if __name__ == '__main__':
    main()
