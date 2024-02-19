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
    customer = Customer("HP",46,"hp@mail.com","321-123-456")
    customer.display_customer_information()
    customer.create_customer()

    customer2 = Customer()
    customer2.display_customer_information("arthur.doyle@mail.com")

if __name__ == '__main__':
    main()
