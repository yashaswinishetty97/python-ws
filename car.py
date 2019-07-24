class Car:
    def __init__(self,regno,no_gears):
        self.regno=regno
        self.no_gears=no_gears
        self.is_started = False
    def start(self):
        if self.is_started:
            print(f"car is already started")
        else:
            print(f"car with reg no {self.regno} started.....")
            self.is_started = True
    def stop(self):
        if self.is_started :
            print(f"car with reg no{self.regno} stopped.....")
            self.is_started = False
        else :
            print(f"car is already stopped")
    def change_gear(self):
        if self.is_started:
            print(f"car with reg no{self.regno} changed gear....")        
        else:
            print(f"the car is stopped")