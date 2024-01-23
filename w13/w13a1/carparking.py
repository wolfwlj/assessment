from datetime import datetime
import sqlite3
import os
import sys


# parked car class
class ParkedCar:
    # constructor
    def __init__(self, licence_plate, check_in):
        self.licence_plate = licence_plate
        self.check_in = check_in


# car parking machine class
class CarParkingMachine:
    # constructor
    def __init__(self, capacity=10, hourly_rate=2.50, id=1):
        self.id = id
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        # database connection
        self.db_conn = sqlite3.connect(os.path.join(sys.path[0], 'carparkingmachine.db'))
        # create table if not exists
        self.db_conn.execute(
            '''CREATE TABLE IF NOT EXISTS parkings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                car_parking_machine TEXT NOT NULL,
                license_plate TEXT NOT NULL,
                check_in TEXT NOT NULL,
                check_out TEXT DEFAULT NULL,
                parking_fee NUMERIC DEFAULT 0
            );'''
        )
        # cursor to execute queries
        self.cursor = self.db_conn.cursor()
        # get cars from database and store them in a dictionary
        self.parked_cars = self.get_cars(self.id, "check-in")

    # method to get cars from database
    def get_cars(self, id, type, all=True):

        # if want to get all cars, not only the ones that are checked in
        if all:
            self.cursor.execute("SELECT * FROM parkings WHERE car_parking_machine = ?", (id,))
        # else:
        #     self.cursor.execute("SELECT * FROM parkings WHERE car_parking_machine = ? AND check_out IS NULL", (id,))
        # get all rows
        rows = self.cursor.fetchall()
        # create empty dictionary
        cars = {}
        # loop through rows and add cars to dictionary
        for row in rows:
            cars.update({row[2]: ParkedCar(row[2], datetime.strptime(row[3], "%d-%m-%Y %H:%M:%S"))})

        return cars

    # method to get all cars by parking machine id
    def find_by_id(self, id) -> ParkedCar:
        # execute query, get row where id is equal to the given parking machine id
        self.cursor.execute("SELECT * FROM parkings WHERE id = ?", (id,))
        # get row
        row = self.cursor.fetchone()

        # return ParkedCar object
        return ParkedCar(row[2], datetime.strptime(row[3], "%d-%m-%Y %H:%M:%S"))

    # method to find last checkin by license plate
    def find_last_checkin(self, license_plate) -> int:
        # execute query, get row where license plate is equal to the given license plate and check out is null
        self.cursor.execute("SELECT * FROM parkings WHERE license_plate = ? AND check_out IS NULL", (license_plate,))
        # get row
        row = self.cursor.fetchone()
        # return id
        return row[0]

    # method to insert a car into the database
    def insert(self, parked_car: ParkedCar) -> ParkedCar:
        # execute query to insert car into database
        self.cursor.execute(
            "INSERT INTO parkings (car_parking_machine, license_plate, check_in) VALUES (?, ?, ?)",
            (self.id, parked_car.licence_plate, parked_car.check_in.strftime("%d-%m-%Y %H:%M:%S"))
        )
        # commit changes
        self.db_conn.commit()
        # return inserted car
        return parked_car

    # method to update(checkout) a car in the database
    def update(self, parked_car: ParkedCar) -> None:
        # execute query to update car in database
        self.cursor.execute(
            "UPDATE parkings SET check_out = ?, parking_fee = ? WHERE id = ?",
            (parked_car.check_out.strftime("%d-%m-%Y %H:%M:%S"), parked_car.parking_fee, parked_car.id)
        )
        # commit changes
        self.db_conn.commit()

    # method to checkin a car
    def check_in(self, license_plate, check_in=None):
        # if check in is not given, set it to current time
        check_in = datetime.now()
        # if capacity is not reached, insert car into database
        if len(self.get_cars(self.id, "check-in")) < self.capacity:

            # execute query to insert car into database
            self.cursor.execute(
                "INSERT INTO parkings (car_parking_machine, license_plate, check_in) VALUES (?, ?, ?)",
                (self.id, license_plate, check_in.strftime("%d-%m-%Y %H:%M:%S"))
            )
            # commit changes
            self.db_conn.commit()
            # add car to dictionary
            self.parked_cars.update({license_plate: ParkedCar(license_plate, check_in)})

            return True
        # if capacity is reached, return false
        else:
            return False

    # method to checkout a car
    def check_out(self, licence_plate):
        # if license plate is in database, update car
        if licence_plate in self.get_cars(self.id, "check-in"):
            # get parking fee of car by license plate
            parking_fee = self.get_parking_fee(licence_plate)
            # execute query to update car in database/checkout
            self.cursor.execute(
                "UPDATE parkings SET check_out = ?, parking_fee = ? WHERE license_plate = ? AND check_out IS NULL",
                (datetime.now().strftime("%d-%m-%Y %H:%M:%S"), parking_fee, licence_plate)
            )
            # commit changes
            self.db_conn.commit()
            # parking_fee = self.get_parking_fee(licence_plate)

            # remove car from dictionary
            del self.parked_cars[licence_plate]

            return parking_fee
        # if license plate is not in database, return None
        else:
            return None

    # method to get parking fee
    def get_parking_fee(self, licence_plate):
        # get car from dictionary
        car = self.parked_cars[licence_plate]
        # calculate time difference in hours
        # volledige momentele datum met timestamp
        # print(datetime.now())
        # volledige check in datum met timestamp
        # print(self.parked_cars[licence_plate].check_in)
        # verschil in tijd tussen nu en check in
        # print((datetime.now() - self.parked_cars[licence_plate].check_in))
        # verschil in tijd tussen nu en check in naar seconden format veranderen dan / 3600 om naar uren te gaan. 
        time_difference = (datetime.now() - car.check_in).total_seconds() / 3600
        # if time difference is less than 24 hours, calculate fee
        if time_difference < 24:
            # check if time difference is a float
            # if checkfloat is not -1, time difference is a float
            if isinstance(time_difference, float):
                # round up time difference
                time_difference = int(time_difference) + 1

            fee = time_difference * self.hourly_rate
        # else, fee is 24 * hourly rate
        else:
            fee = 24 * self.hourly_rate
        return fee


# main function
def main():
    # create instance of CarParkingMachine
    instancecarmachine = CarParkingMachine(10, 2.50)
    # loop through menu
    while True:
        print("[I] Check-in car by license plate")
        print("[O] Check-out car by license plate")
        print("[Q] Quit program")

        actie = input("Wat wilt u doen?")
        # if I is pressed, start process to checkin a car
        if actie.lower() == 'i':
            licenseplate = input("vul een kenteken in")

            if instancecarmachine.check_in(license_plate=licenseplate):
                print("License registered")
            else:
                print("Capacity reached")
        # if O is pressed, start process to checkout a car
        elif actie.lower() == 'o':
            licenseplate = input("vul een kenteken in")
            fee = instancecarmachine.check_out(licenseplate)
            print(f"parking fee : {fee:.2f} EUR")
        # if Q is pressed, quit the program
        elif actie.lower() == 'q':
            break
        else:
            print("invalid input")


if __name__ == "__main__":
    main()