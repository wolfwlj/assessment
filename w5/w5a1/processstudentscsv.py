import os
import sys

valid_lines = []
corrupt_lines = []

'''
The validate_data function will check the students.csv line by line for corrupt data.
- Valid lines should be added to the valid_lines list.
- Invalid lines should be added to the corrupt_lines list.
Example input: 0896801,Kari,Wilmore,1970-06-18,INF
This data is valid and the line should be added to the valid_lines list unchanged.
Example input: 0773226,Junette,Gur_ry,1995-12-05,
This data is invalid and the line should be added to the corrupt_lines list in the following format:
0773226,Junette,Gur_ry,1995-12-05, => INVALID DATA: ['0773226', 'Gur_ry', '']
In the above example the studentnumber does not start with '08' or '09',
the last name contains a special character and the student program is empty.
Don't forget to put the students.csv file in the same location as this file!
'''


def validate_data(line):
    # WRITE YOUR SOLUTION HERE:

    gesplit = line.split(",")
    split_date = gesplit[3].split("-")
    allowed_study_programs = ["INF", "TINF", "CMD", "AI"]
    invalid_delen = []
    nietcorrupt = True

    iteratie = 0
    for deel in gesplit:
        if deel == "":
            invalid_delen.append(gesplit[iteratie])
            nietcorrupt = False
        iteratie += 1

    if len(invalid_delen) > 0:
        invalid_volledig = f"{line} => INVALID DATA: {invalid_delen}"
        corrupt_lines.append(invalid_volledig)
        return

    if len(gesplit[0]) > 7:
        invalid_delen.append(gesplit[0])
        nietcorrupt = False

    if gesplit[0][0] != "0" or gesplit[0][1] != "8" and gesplit[0][1] != "9":
        invalid_delen.append(gesplit[0])
        print(gesplit[0][1])
        nietcorrupt = False

    if gesplit[1].isalpha() is False:
        invalid_delen.append(gesplit[1])
        nietcorrupt = False

    if gesplit[2].isalpha() is False:
        invalid_delen.append(gesplit[2])
        nietcorrupt = False

    if gesplit[4] not in allowed_study_programs:
        invalid_delen.append(gesplit[4])
        nietcorrupt = False

    if 1960 > int(split_date[0]) or 2004 < int(split_date[0]) or 1 > int(split_date[1]) or 12 < int(split_date[1]):

        invalid_delen.append(gesplit[3])
        nietcorrupt = False

    if 1 > int(split_date[2]) or 31 < int(split_date[2]):

        invalid_delen.append(gesplit[3])
        nietcorrupt = False

    if len(split_date[0]) != 4:
        invalid_delen.append(gesplit[3])
        nietcorrupt = False

    if nietcorrupt:
        valid_lines.append(line)

    if len(invalid_delen) > 0:
        invalid_volledig = f"{line} => INVALID DATA: {invalid_delen}"
        corrupt_lines.append(invalid_volledig)


def main(csv_file):
    with open(os.path.join(sys.path[0], csv_file), newline='') as csv_file:
        # skip header line
        next(csv_file)

        for line in csv_file:
            validate_data(line.strip())

    print('### VALID LINES ###')
    print("\n".join(valid_lines))
    print('### CORRUPT LINES ###')
    print("\n".join(corrupt_lines))


if __name__ == "__main__":
    main('students.csv')