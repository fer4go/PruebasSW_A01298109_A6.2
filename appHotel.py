"""
"""
from app.hotel import Hotel
from app.customer import Customer
from app.reservation import Reservation
from app.app_utils import appUtils


def main():
    """
    main test function
    """
    print("main")

    customer = Customer("hp2@mail.com","HP",46,"321-123-456")
    #customer.get_customer_information()
    customer.create_customer()
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

    #customer.delete_customer()
    #customer.get_customer_information("hp@mail.com")
    #customer.display_customer_information()
##
    #hotel = Hotel("The Hostel", "the City", 3, "Hostal")
    #hotel.create_hotel()
    #hotel.get_hotel_information("The Hostal")
    #hotel.display_hotel_information()

    #hotel.modify_hotel_information("The Hostel", "at City", "Hostal", 5)
    #hotel.display_hotel_information()

    #hotel.delete_hotel()
    #reserve = Reservation("The Hostel", "bram.stoker@mail.com", 2)
    #reserve.create_reservation()
    #reserve.cancel_reservation()
    # hotel.show_all_reservations()
    #hotel.display_hotel_information()

if __name__ == '__main__':
    main()
