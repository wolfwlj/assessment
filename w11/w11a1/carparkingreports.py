def main():
    print("[P] Report all parked cars during a parking period for a specific parking machine")
    print("[F] Report total collected parking fee during a parking period for all parking machines")
    print("[Q] Quit program")

    while True:

        actie = input("Wat wilt u doen?")   


        if actie.lower() == 'p':
            # start_date = input("vul een start datum in")
            # end_date = input("vul een eind datum in")
            # licenseplate = input("vul een kenteken in")
            # fee = instancecarmachine.get_machine_fee_by_day(licenseplate, start_date, end_date)
            # print(f"parking fee : {fee:.2f} EUR")
            print("not implemented yet")
        elif actie.lower() == 'o':
            print("not implemented yet")
        elif actie.lower() == 'q':
            break
        else:
            print("invalid input")


if __name__ == "__main__":
    main()