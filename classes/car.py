class  Car:
    wheel = 4
    def __init__(self,make,model,color):
        self.make = make
        self.model = model
        self.color = color
    def hooting(self,hoot):
        self.hoot = hoot
        return f"The {self.color},{self.make} {self.hoot}"
    def speed(self,accelerate):
        self.accelerate = accelerate
        return f"i drove the car at {self.accelerate} km/hr"
    def get_model(self):
        return f"my car is of type {self.model}"
car = Car(make="Nissan",model="Altima",color="blue")
print(car.hooting(hoot="honks"))
car2 = Car(make="Audi",model="A3",color="grey")
print(car2.speed(accelerate=70))
car3 = Car(make="Toyota",model="Airwave",color="black")
print(car3.get_model())



