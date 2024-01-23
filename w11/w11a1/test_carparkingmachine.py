from carparking import *
from datetime import datetime, timedelta

# Test for a normal check-in with correct result (True)
def test_check_in_capacity_normal():
    obj_CarParkingMachine = CarParkingMachine (60, 2.5) 
    obj_CarParkingMachine.check_in("Auto1")
    assert True == obj_CarParkingMachine.check_in("Auto2")


# Test for a check-in with maximum capacity reached (False)
def test_check_in_capacity_reached():
    obj_CarParkingMachine = CarParkingMachine (3, 2.5) 
    obj_CarParkingMachine.check_in("Auto1") 
    obj_CarParkingMachine.check_in("Auto2")
    obj_CarParkingMachine.check_in("Auto3")

    assert False == obj_CarParkingMachine.check_in("")


# Test for checking the correct parking fees
def test_parking_fee():
    #creeren van een object
    obj_CarParkingMachine = CarParkingMachine(10, 2.5)
    # Assert that parking time 2h10m, gives correct parking fee
    obj_CarParkingMachine.check_in("Auto1", datetime.now() - timedelta(hours=2, minutes=10))
    assert obj_CarParkingMachine.check_out("Auto1") == 7.5 

    # Assert that parking time 24h, gives correct parking fee
    obj_CarParkingMachine.check_in("Auto2", datetime.now() - timedelta(hours=24))
    assert obj_CarParkingMachine.check_out("Auto2") == 60

    # Assert that parking time 30h == 24h max, gives correct parking fee
    obj_CarParkingMachine.check_in("Auto3", datetime.now() - timedelta(hours=30))
    assert obj_CarParkingMachine.check_out("Auto3") == 60


# Test for validating check-out behaviour
def test_check_out():
    obj_testcheckout = CarParkingMachine(10, 2.5)
    obj_testcheckout.check_in("Auto1")

    # Assert that {license_plate} is in parked_cars
    assert "Auto1" in obj_testcheckout.parked_cars

    # Assert that correct parking fee is provided when checking-out {license_plate}
    assert obj_testcheckout.check_out("Auto1") ==  2.5

    # Aseert that {license_plate} is no longer in parked_cars
    assert "Auto1" not in obj_testcheckout.parked_cars


# Test for validating check-in behaviour
test_check_in_capacity_normal()
test_check_in_capacity_reached()
test_parking_fee()
test_check_out()