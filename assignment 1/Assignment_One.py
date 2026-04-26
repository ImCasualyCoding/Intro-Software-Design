##############################################
# This whole first chunch creates the classes of different ride types 
# and defines a function to calculate fare based on ride type and distance.



class customers:
    def __init__(self, name, distance,ride_type):
        self.name = name
        self.distance = distance
        self.ride_type= ride_type
     

def calculate_fare(ride_type, distance):
    return ride_type.ride_fare(distance)


class Economy :
   def ride_fare(self, distance):
       return distance *5 
   
class Luxury :
   def ride_fare(self, distance):
       return distance *10
   
class Pool :
   def ride_fare(self, distance):
       return distance *3
   

#This is the single responsibility principle applied to the Driver class. It only manages driver-related attributes and does not handle ride requests or fare calculations.
class Driver:
    def __init__(self, name, driver_id):
         self.name = name
         self.driver_id=driver_id
         self.is_occupied = False

#An example of polymorphism where the Driver_Manager class can handle different ride types through a common interface.
class Driver_Manager:
    def __init__(self,driver_list):
        self.driver_list=driver_list

    def requesting_ride(self, ride_type, distance):
        cost= ride_type.ride_fare(distance)

        avaliable_drivers = next((driver for driver in self.driver_list if not driver.is_occupied), None)

        if avaliable_drivers:
            avaliable_drivers.is_occupied = True
            return f"Ride Fare: ${cost}, Driver: {avaliable_drivers.name}"
        return "No drivers available at the moment."
    



if __name__ == "__main__":
    drivers = [
        #numbered drivers for identification
        Driver("Alice", 1),
        Driver("Bob", 2)
    ]

    driver_manager = Driver_Manager(drivers)
    customer_list = [
        customers("John", 15, Economy()),
        customers("Rebeca",10, Luxury()),
        customers("Mike", 5, Pool())
    ]

    for customer in customer_list:
        result = driver_manager.requesting_ride(customer.ride_type, customer.distance)
        print(f"Customer: {customer.name}, {result}")


