class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.available = True

class CarRentalSystem:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def rent_car(self, make, model, year):
        for car in self.cars:
            if car.make == make and car.model == model and car.year == year and car.available:
                car.available = False
                return car
        return None

    def return_car(self, car):
        car.available = True

    def display_cars(self):
        print("\nAvailable Cars:")
        for car in self.cars:
            if car.available:
                print(f"{car.year} {car.make} {car.model}")

if __name__ == '__main__':
    rental_system = CarRentalSystem()

    car1 = Car("Toyota", "Camry", 2020)
    car2 = Car("Honda", "Civic", 2021)

    rental_system.add_car(car1)
    rental_system.add_car(car2)

    while True:
        print("\nCar Rental System")
        print("1. Rent Car")
        print("2. Return Car")
        print("3. Display Available Cars")
        print("4. Quit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            rental_system.display_cars()
            make = input("Enter car make: ")
            model = input("Enter car model: ")
            year = int(input("Enter car year: "))
            car = rental_system.rent_car(make, model, year)
            if car:
                print(f"You have rented a {car.year} {car.make} {car.model}.")
            else:
                print("Car not available.")
        elif choice == '2':
            make = input("Enter car make: ")
            model = input("Enter car model: ")
            year = int(input("Enter car year: "))
            for car in rental_system.cars:
                if car.make == make and car.model == model and car.year == year and not car.available:
                    rental_system.return_car(car)
                    print(f"You have returned the {car.year} {car.make} {car.model}.")
                    break
            else:
                print("Car not found or not rented.")
        elif choice == '3':
            rental_system.display_cars()
        elif choice == '4':
            print("Goodbye!")
            break
