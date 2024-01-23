dict_key_value = {}
encoded_values = []
decoded_values = []


def printallvalues():
    print("encoded values: ", encoded_values)
    print("decoded values: ", decoded_values)


# create a function that given the input string converts it to
# the encoded equivalent based on the provided or already set key/hashmap
# make sure to only convert values that are in the key, if the value is not present, use its own value
def encode_string(hash_data: str, key: str = None) -> str:
    # an example of a key is :  A%B&C(D)E*F+G-H/I0J<K=L1M!N9O?P>Q7R#S5T;U:V[W]X~Y$Z@

    chardict = dict(zip(key[::2], key[1::2]))
    encoded_string = ""
    for char in hash_data:
        if char in chardict:
            encoded_string += chardict[char]

    encoded_values.append(encoded_string)
    return encoded_string


# create a function that given the input string converts it to the
# decoded equivalent based on the provided or already set key/hashmap
# make sure to only decode values that are in the key, if the value is not present, use its own value
def decode_string(hash_data: str, key: str = None) -> str:
    chardict = dict(zip(key[1::2], key[::2]))
    # print(chardict)
    decoded_string = ""
    hash_data = hash_data.upper()
    for char in hash_data:
        if char in chardict:
            decoded_string += chardict[char]

    decoded_values.append(decoded_string)
    return decoded_string


# create a function that given a list of inputs converts
# the complete list to the encoded equivalent based on the key/hashmap
# you can use the already created encode function when looping through the list
# tip! make use of the map function within python with a lambda to call the internal function with all elements
# as a return value, you should return a list with the converted values
def encode_list(hash_data: list, key: str = None) -> list:
    chardict = dict(zip(key[::2], key[1::2]))
    encode_string_list = []
    hash_data = hash_data.upper()
    for hash_data_item in hash_data:
        encoded_string = ""
        hash_data = hash_data.upper()
        for char in hash_data_item:
            if char in chardict:
                encoded_string += chardict[char]
        encode_string_list.append(encoded_string)

    print(encoded_string)
    return encode_string_list


# create a function that given a list of inputs converts the complete list
# to the encoded equivalent based on the key/hashmap
# you can use the already created decode function when looping through the list
# tip! make use of the map function within python with a lambda to call the internal function with all elements
# as a return value, you should return a list with the converted values
def decode_list(hash_data: list, key: str = None) -> list:
    decoded_string_list = []
    hash_data = hash_data.upper()

    for hash_data_item in hash_data:
        # decoded_string = ""
        # for char in hash_data_item:
        #     if char in chardict:
        #         decoded_string_list += chardict[char]
        decoded_string_list.append(lambda x: decode_string(hash_data_item, key))

    print(decoded_string_list)
    return decoded_string_list


# create a function that given a encoded value, decoded value and a key (optional) checks if the values are correct
# the return value should be a boolean value (True if values match, False if they don't match)
def validate_values(encoded: str, decoded: str, key: str = None) -> bool:

    chardict = dict(zip(key[1::2], key[::2]))

    decoded_string = ""

    for char in encoded:
        if char in chardict:
            decoded_string += chardict[char]

    if decoded_string != decoded:
        print("False")

        return False
    else:
        print("True")

        return True


# give the option to input a hashvalue to be used/converted to a key
# each oneven character is the Key of the Dict, each even character is the coresponding Value
# you should validate if the given input is an even input, otherwise show the error: Invalid hashvalue input
# example: a@b.c>d#eA will become: {'a': '@', 'b': '.', 'c': '>', 'd', '#', 'e': 'A'}
def set_dict_key(key: str) -> None:
    if len(key) % 2 != 0:
        print("Invalid hashvalue input")
        return
    chardict = dict(zip(key[1::2], key[::2]))
    print(chardict)
    return chardict


# build menu structure as following
# the input can be case-insensitive (so E and e are valid inputs)
# [E] Encode value to hashed value
# [D] Decode hashed value to normal value
# [P] Print all encoded/decoded values
# [V] Validate 2 values against eachother
# [Q] Quit program
def main():

    while True:
        hash_input = input("key:")

        print("""[E] Encode value to hashed value
[D] Decode hashed value to normal value
[P] Print all encoded/decoded values
[V] Validate 2 values against eachother
[Q] Quit program""")
        if hash_input == "a_b?c9d6e1f4g!h:i<j|k{l0m@n7o+p~":
            pass
        elif len(hash_input) != 52:
            print("Invalid hashvalue input")
            break

        actie = input("Wat wilt u doen?")

        if actie.upper() == "E":
            keyinput = input("hash:")
            encode_string(keyinput, hash_input)

        elif actie.upper() == "D":
            keyinput = input("hash:")
            decode_string(keyinput, hash_input)

        elif actie.upper() == "P":
            printallvalues()
        elif actie.upper() == "V":
            encoded_hash_data = input("hash:")
            decoded_hash_data = input("hash:")
            validate_values(encoded_hash_data, decoded_hash_data, hash_input)
            print("validate")
        elif actie.upper() == "Q":
            print("quit")
            break
        else:
            print("ongeldige actie")

        actie_twee = input("Wat wilt u doen?")
        if actie_twee.upper() == "P":
            printallvalues()
        elif actie_twee.upper() == "Q":
            print("quit")
            break
        else:
            print("ongeldige actie")

        actie_drie = input("Wat wilt u doen?")
        if actie_drie.upper() == "Q":
            print("quit")
            break
        elif actie_drie.upper() == "P":
            printallvalues()


# Create a unittest for both the encode and decode function (see test_namehasher.py file for boilerplate)
if __name__ == "__main__":
    main()