import datetime


class ParkedCar:
    def __init__(self, licence_plate, check_in):
        self.licence_plate = licence_plate
        self.check_in = check_in


class CarParkingMachine:
    def __init__(self, capacity=10, hourly_rate=2.50, id=1):
        self.id = id
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        self.parked_cars = {}
        self.logger = CarParkingLogger(id)

    def check_in(self, license_plate, check_in=datetime.datetime.now()):
        if len(self.parked_cars) < self.capacity:
            self.parked_cars[license_plate] = ParkedCar(license_plate, check_in)
            self.logger.write_to_log(license_plate, "check-in", check_in)
            return True
        else:
            return False

    def check_out(self, licence_plate=""):
        parking_fee = self.get_parking_fee(licence_plate)
        del self.parked_cars[licence_plate]
        self.logger.write_to_log(licence_plate, "check-out", datetime.datetime.now(), parking_fee)

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

class CarParkingLogger:
    def __init__(self, id) -> None:
        self.id = id

    def get_machine_fee_by_day(self, car_parking_machine_id, search_date):
        # if bool(datetime.strptime(search_date, "%d-%m-%Y")) is False:
        #     return 0.0
        fee = 0

        cars = self.get_cars(car_parking_machine_id, "check-out")

        for car_data in cars:
            fulldate = datetime.strptime(search_date, "%d-%m-%Y %H:%M:%S")
            correct_date = datetime.strptime(fulldate, format)
            if correct_date == search_date:
                fee += float(car_data[1])

        return round(fee, 2)

    def get_total_car_fee(self, license_plate):
        fee = 0.0
        cars = self.get_cars(self.id, "check-out", True)

        for temp_licence, car_data in cars.items():
            license = temp_licence.split("#")[0]

            if license == license_plate:
                fee += float(car_data[1])

        return fee

    def write_to_log(self, license_plate="", actie_type="", check_in=datetime.datetime.now(), fee=0.0):

        defaulttype = "check-in"
        if actie_type == "check-out":
            defaulttype = f"check-out;parking_fee={fee}"

        date = check_in.strftime("%d-%m-%Y %H:%M:%S")

        with open("carparklog.txt", "a") as log_file:
            log_file.write(f"{date};cpm_name={self.id};license_plate={license_plate};action={defaulttype}\n")


def main():
    instancecarmachine = CarParkingMachine(10, 2.50)

    while True:

        print("[I] Check-in car by license plate")
        print("[O] Check-out car by license plate")
        print("[Q] Quit program")

        actie = input("Wat wilt u doen?")

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