
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")



class Car(Vehicle):
    def move(self):
        print("Driving on the road...")


class Plane(Vehicle):
    def move(self):
        print("Flying through the sky...")


class Boat(Vehicle):
    def move(self):
        print("Sailing on the water...")


class Bicycle(Vehicle):
    def move(self):
        print("Pedaling along the path...")



vehicles = [Car(), Plane(), Boat(), Bicycle()]

for v in vehicles:
    v.move()   
