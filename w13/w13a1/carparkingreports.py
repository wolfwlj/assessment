# Adjust CarParkingReporter:
# Adjust the carparkingreporter in such a way that it uses the database for the reports

# Add the following menu item to carparkingreport:
# [C] Report all complete parkings over all parking machines for a specific car

# Input: license_plate
# Output: csv file example (semicolon separated):

# car_parking_machine;check_in;check_out;parking_fee 
# cpm_north;09-21-2022 16:20:04;09-21-2022 17:20:30;5.00
# cpm_south;09-22-2022 14:11:03;09-23-2022 19:00:10;15.00

from datetime import datetime
import csv
import sqlite3
import sys

def create_csv_file(data, filename):
    #prevent dict items object is not subscriptable
    data = list(data)
    fieldnames = list(data[0].keys())


    with open(f"{filename}.csv", "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames, delimiter=";")
        writer.writeheader()
        writer.writerows(data)


def get_specific_period(cursor, machine, from_date, to_date):
    cursor.execute("SELECT * FROM parkings WHERE car_parking_machine = ? AND check_in BETWEEN ? AND ? AND check_out IS NOT NULL ORDER BY check_in ASC", (machine, from_date, to_date))
    rows = cursor.fetchall()
    cars = []
    for row in rows:
        cars.append({
            "license_plate": row[2],
            "checked_in": row[3],
            "checked_out": row[4],
            "parking_fee": row[5]
        })

    create_csv_file(cars[::-1], f"parkedcars_{machine}_from_{from_date}_to_{to_date}")



def get_all_fees(cursor, from_date, to_date):
    cursor.execute("SELECT * FROM parkings WHERE check_in BETWEEN ? AND ?", (from_date, to_date))
    rows = cursor.fetchall()
    fees = []
    for row in rows:
        names = {machine['car_parking_machine'] for machine in fees}
        if row[1] not in names:
            fees.append({"car_parking_machine": row[1], "total_parking_fee": float(row[5])})
        else:
            machine = next((fee for fee in fees if fee['car_parking_machine'] == row[1]), None)
            machine['total_parking_fee'] += float(row[5])
        
    create_csv_file(fees, f"totalfee_from_{from_date}_to_{to_date}")

def get_cars_in_period(cursor, from_date, to_date):
    cursor.execute("SELECT * FROM parkings WHERE check_in BETWEEN ? AND ?", (from_date, to_date))
    rows = cursor.fetchall()
    cars = {}
    for row in rows:
        cars.update({row[2]: row})

    create_csv_file(cars.values(), f"parkedcars_from_{from_date}_to_{to_date}")


def main():
    conn = sqlite3.connect("carparkingmachine.db")
    cursor = conn.cursor()

    print("[P] Report all parked cars during a parking period for a specific parking machine")
    print("[F] Report total collected parking fee during a parking period for all parking machines")
    print("[C] Report all complete parkings over all parking machines for a specific car")
    print("[Q] Quit program")

    while True:

        choice = input("Enter your choice: ").upper()

        if choice == "P":
            # data is in a single input, example : South,10-11-2022,12-11-2022
            data = input("Enter parking machine, start date and end date: ").split(",")
            machine = data[0]
            from_date = data[1]
            to_date = data[2]

            get_specific_period(cursor, machine, from_date, to_date)

        elif choice == "F":
            # data is in a single input, example : 10-11-2022,12-11-2022
            data = input("Enter start date and end date: ").split(",")
            from_date = data[0]
            to_date = data[1]

            get_all_fees(cursor, from_date, to_date)

        elif choice == "C":

            license_plate = input("Enter license plate: ")

            cursor.execute("SELECT * FROM parkings WHERE license_plate = ? AND check_out IS NOT NULL ORDER BY check_in DESC", (license_plate,))
            rows = cursor.fetchall()

            cars = []

            for row in rows:
                cars.append({
                    "car_parking_machine": row[1],
                    "check_in": row[3],
                    "check_out": row[4],
                    "parking_fee": row[5]
                })

            create_csv_file(cars, f"all_parkings_for_{license_plate}")

        elif choice == "Q":
            break


if __name__ == "__main__":
    main()