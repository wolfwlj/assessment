import datetime


class ParkedCar:
    def __init__(self, licence_plate, check_in):
        self.licence_plate = licence_plate
        self.check_in = check_in


class CarParkingMachine:
    def __init__(self, capacity=10, hourly_rate=2.50):
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        self.parked_cars = {}

    def check_in(self, license_plate, time=datetime.datetime.now()):
        if len(self.parked_cars) < self.capacity:
            self.parked_cars[license_plate] = ParkedCar(license_plate, time)
            return True
        else:
            return False

    def check_out(self, licence_plate):
        parking_fee = self.get_parking_fee(licence_plate)
        del self.parked_cars[licence_plate]

        return float(parking_fee)

    def get_parking_fee(self, licence_plate):
        # volledige momentele datum met timestamp
        # print(datetime.now())
        # volledige check in datum met timestamp
        # print(self.parked_cars[licence_plate].check_in)
        # verschil in tijd tussen nu en check in
        # print((datetime.now() - self.parked_cars[licence_plate].check_in))
        # verschil in tijd tussen nu en check in naar seconden format veranderen dan / 3600 om naar uren te gaan. 
        time_difference = (datetime.datetime.now() - self.parked_cars[licence_plate].check_in).total_seconds() / 3600
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


def main():
    instancecarmachine = CarParkingMachine(10, 2.50)

    while True:
        actie = input("""[I] Check-in car by license plate
[O] Check-out car by license plate
[Q] Quit program""")

        if actie.lower() == 'i':
            licenseplate = input("vul een kenteken in")

            if instancecarmachine.check_in(license_plate=licenseplate):
                print("License registered")
            else:
                print("Capacity reached")
        elif actie.lower() == 'o':
            licenseplate = input("vul een kenteken in")
            fee = instancecarmachine.check_out(licenseplate)
            print(f"parking fee : {fee:.2f} EUR")

        elif actie.lower() == 'q':
            break
        else:
            print("invalid input")


if __name__ == "__main__":
    main()