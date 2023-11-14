########################   Shapes ########################
class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        # luat de pe net
        s = (self.side1 + self.side2 + self.side3) / 2
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3))**0.5

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

########################   Bank ########################

class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def calculate_interest(self):
        pass

class SavingsAccount(Account):
    def calculate_interest(self):
        return 0.02 * self.balance

class CheckingAccount(Account):
    def calculate_interest(self):
        return 0.01 * self.balance


########################   Vehicle ########################


class Vehicle:
    def __init__(self, make, model, year,consuption,fuel):
        self.make = make
        self.model = model
        self.year = year
        self.consuption=consuption
        self.fuel=fuel
    def calculate_mileage(self):
        pass

    def calculate_towing_capacity(self):
        pass

class Car(Vehicle):
    def calculate_mileage(self):
        # Verificăm pentru a evita împărțirea la zero
        if self.consuption != 0:
            return self.fuel * (self.consuption/100)
        else:
            return 0 

class Motorcycle(Vehicle):
    def calculate_mileage(self):
        # Verificăm pentru a evita împărțirea la zero
        if self.consuption != 0:
            return self.fuel * (self.consuption/100)
        else:
            return 0 

class Truck(Vehicle):
    def calculate_mileage(self):
        # Verificăm pentru a evita împărțirea la zero
        if self.consuption != 0:
            return self.fuel  *(self.consuption/100)
        else:
            return 0 

    def calculate_towing_capacity(self):
        
        return 45000  




class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary

    def display_info(self):
        print(f"Name: {self.name}\nSalary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def manage_team(self):
        print(f"{self.name} is managing a team of {self.team_size} members.")

    def display_info(self):
        super().display_info()
        print(f"Role: Manager")

class Engineer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def write_code(self):
        print(f"{self.name} is writing code in {self.programming_language}.")

    def display_info(self):
        super().display_info()
        print(f"Role: Engineer")

class Salesperson(Employee):
    def __init__(self, name, salary, sales_target):
        super().__init__(name, salary)
        self.sales_target = sales_target

    def make_sales(self):
        print(f"{self.name} is making sales to achieve a target of {self.sales_target}.")

    def display_info(self):
        super().display_info()
        print(f"Role: Salesperson")








class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        pass  

class Mammal(Animal):
    def give_birth(self):
        return "The mammal gives birth to live young."

    def make_sound(self):
        return "Mammal sound"

class Bird(Animal):
    def fly(self):
        return "The bird is flying."

    def make_sound(self):
        return "Birdsong"

class Fish(Animal):
    def swim(self):
        return "The fish is swimming."

    def make_sound(self):
        return "No sound"  







class LibraryItem:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.checked_out = False

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            print(f"{self.title} checked out successfully.")
        else:
            print(f"{self.title} is already checked out.")

    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            print(f"{self.title} returned successfully.")
        else:
            print(f"{self.title} is not checked out.")

class Book(LibraryItem):
    def __init__(self, title, author, year, genre):
        super().__init__(title, author, year)
        self.genre = genre

class DVD(LibraryItem):
    def __init__(self, title, director, year, duration):
        super().__init__(title, director, year)
        self.duration = duration

class Magazine(LibraryItem):
    def __init__(self, title, publisher, year, issue_number):
        super().__init__(title, publisher, year)
        self.issue_number = issue_number



circle = Circle(radius=5)
rectangle = Rectangle(length=4, width=6)
triangle = Triangle(side1=3, side2=4, side3=5)


print()
print("###################################################################")
print()
print(f"Circle - Area: {circle.area()}, Perimeter: {circle.perimeter()}")
print(f"Rectangle - Area: {rectangle.area()}, Perimeter: {rectangle.perimeter()}")
print(f"Triangle - Area: {triangle.area()}, Perimeter: {triangle.perimeter()}")

print()
print("###################################################################")
print()





savings_account = SavingsAccount(balance=1000)
checking_account = CheckingAccount(balance=1500)


savings_account.deposit(500)
savings_account.withdraw(200)
checking_account.deposit(1000)
checking_account.withdraw(2000)


print(f"Savings Account - Interest: {savings_account.calculate_interest()}")
print(f"Checking Account - Interest: {checking_account.calculate_interest()}")
print()
print("###################################################################")
print()






car_instance = Car(make="Audi", model="A5", year=2012, consuption=10, fuel=50)
car_mileage = car_instance.calculate_mileage()
print(f"Car Mileage: {car_mileage} km")


motorcycle_instance = Motorcycle(make="BMW", model="Z", year=2023, consuption=5, fuel=20)
motorcycle_mileage = motorcycle_instance.calculate_mileage()
print(f"Motorcycle Mileage: {motorcycle_mileage} km")


truck_instance = Truck(make="Scania", model="F150", year=2020, consuption=15, fuel=80)
truck_mileage = truck_instance.calculate_mileage()
print(f"Truck Mileage: {truck_mileage} km")

print()
print("###################################################################")
print()




# Exemplu de utilizare
manager = Manager(name="John Manager", salary=80000, team_size=10)
engineer = Engineer(name="Alice Engineer", salary=60000, programming_language="Python")
salesperson = Salesperson(name="Bob Salesperson", salary=50000, sales_target=100000)

manager.display_info()
manager.manage_team()
print("\n")

engineer.display_info()
engineer.write_code()
print("\n")

salesperson.display_info()
salesperson.make_sales()




print()
print("###################################################################")
print()





mammal = Mammal(species="Lion")
bird = Bird(species="Eagle")
fish = Fish(species="Salmon")


print(f"{mammal.species}: {mammal.give_birth()} {mammal.make_sound()}")
print(f"{bird.species}: {bird.fly()} {bird.make_sound()}")
print(f"{fish.species}: {fish.swim()} {fish.make_sound()}")



print()
print("###################################################################")
print()




book = Book(title="Luceafarul", author="M Eminescu", year=1925, genre="Poetry")
dvd = DVD(title="Miami beach", director="Bromania", year=2016, duration=148)
magazine = Magazine(title="CanCan", publisher="Adevarul", year=2022, issue_number=5)


book.check_out()
dvd.check_out()
magazine.return_item()


print(f"Book - Checked Out: {book.checked_out}")
print(f"DVD - Checked Out: {dvd.checked_out}")
print(f"Magazine - Checked Out: {magazine.checked_out}")

