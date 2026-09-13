# Assignment 7 - Program 4
# Transport, Boat and Bus using Inheritance

class Transport:
    def __init__(self, transport_type):
        self.transport_type = transport_type

    def show(self):
        print("Type of Transport:", self.transport_type)


class Boat(Transport):
    def __init__(self, transport_type, capacity, source, destination):
        super().__init__(transport_type)
        self.capacity = capacity
        self.source = source
        self.destination = destination

    def show(self):
        super().show()
        print("Capacity:", self.capacity)
        print("Source:", self.source)
        print("Destination:", self.destination)


class Bus(Transport):
    def __init__(self, transport_type, seats, source, destination):
        super().__init__(transport_type)
        self.seats = seats
        self.source = source
        self.destination = destination

    def show(self):
        super().show()
        print("Number of Seats:", self.seats)
        print("Source:", self.source)
        print("Destination:", self.destination)


# Create two Boat objects
boat1 = Boat("Water Transport", 100, "Kolkata", "Port Blair")
boat2 = Boat("Water Transport", 150, "Mumbai", "Goa")

# Create two Bus objects
bus1 = Bus("Road Transport", 40, "Kolkata", "Durgapur")
bus2 = Bus("Road Transport", 50, "Delhi", "Agra")


# Display Boat records
print("----- BOAT 1 -----")
boat1.show()

print("\n----- BOAT 2 -----")
boat2.show()


# Display Bus records
print("\n----- BUS 1 -----")
bus1.show()

print("\n----- BUS 2 -----")
bus2.show()
