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
    custo3 = Customer("CustomerName3",23,"customer@example.com","321-123-456")
    custo2 = Customer()
    custo2.display_customer_information("data/customers.json","customer.name1@example.com")

if __name__ == '__main__':
    main()
