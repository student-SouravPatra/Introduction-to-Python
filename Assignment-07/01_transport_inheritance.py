# Assignment 7 - Transport Inheritance
# Demonstration of Inheritance

class Transport:
    def getval(self):
        self.type = input("Enter type of transport: ")

    def show(self):
        print("Type of Transport:", self.type)


class Bus(Transport):
    def getval(self):
        super().getval()

        self.seat_no = int(input("Enter number of seats: "))
        self.source = input("Enter source: ")
        self.destination = input("Enter destination: ")

    def display(self):
        self.show()
        print("Number of Seats:", self.seat_no)
        print("Source:", self.source)
        print("Destination:", self.destination)


# Create Bus object
bus = Bus()

# Get values
bus.getval()

# Display all values
print("\n--- Bus Details ---")
bus.display()
