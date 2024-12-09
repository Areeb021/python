class Car:
    def __init__(self, make, model, year, mileage=0):
     
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
    
    def display_info(self):
       
        print(f"Car Info: {self.year} {self.make} {self.model}")
        print(f"Mileage: {self.mileage} miles")
    
    def drive(self, miles):
      
        self.mileage += miles
        print(f"Car driven for {miles} miles. Total mileage is now {self.mileage} miles.")


car1 = Car("Toyota", "Corolla", 2020)
car1.display_info()  
car1.drive(100) 
car1.display_info() 
