from carparking import CarParkingMachine


def test_check_in_single_parking_machine_only():
    east = CarParkingMachine(id='East')

    westwestnorth = CarParkingMachine(id='WestWestNorth')

    assert True is east.check_in(license_plate='checkin_test1')

    assert True is ('checkin_test1' in east.parked_cars)

    assert True is east.check_in(license_plate='checkin_test2')

    assert True is ('checkin_test2' in east.parked_cars)

    # assert False is westwestnorth.check_in(license_plate='checkin_test1')



def test_restore_state_json():
    westwestnorth = CarParkingMachine(id='WestWestNorth')

    east = CarParkingMachine(id='East')

    assert True is ('checkin_test1' in east.parked_cars)
    assert True is ('checkin_test2' in east.parked_cars)

    east.check_out('checkin_test1')
    assert False is ('checkin_test1' in east.parked_cars)

    east.check_out('checkin_test2')
    assert False is ('checkin_test2' in east.parked_cars)

    assert True is westwestnorth.check_in(license_plate='checkin_test2')