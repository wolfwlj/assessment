# im going to add comments to this entire file to make it easier to understand


# create a global variable that will be used as a key/hashmap
dict_key_value = {}
# create a global variable that will be used to store all encoded values
encoded_values = []
# create a global variable that will be used to store all decoded values
decoded_values = []


# create a function that prints all encoded and decoded values
def printallvalues():
    print("encoded values: ", encoded_values)
    print("decoded values: ", decoded_values)


# create a function that given the input string converts it to
# the encoded equivalent based on the provided or already set key/hashmap
# make sure to only convert values that are in the key, if the value is not present, use its own value
def encode_function(hash_data: str) -> str:
    # default key
    key = "a_b?c9d6e1f4g!h:i<j|k{l0m@n7o+p~q2r+s/t=u^v3w]x(y-z>A*B8C;D%E#F}G5H)I[J$"
    # here we are creating a dictionary with with every uneven character as a key and every even character as a value
    chardict = dict(zip(key[::2], key[1::2]))
    encoded_string = ""
    # loop through the hash_data and check if the character is in the dictionary, if it is,
    # add the value to the encoded_string
    for char in hash_data:
        if char in chardict:
            encoded_string += chardict[char]
    # add the encoded_string to the encoded_values list
    encoded_values.append(encoded_string)
    # return the encoded_string
    return encoded_string


# create a function that given the input string converts it to the decoded equivalent
# based on the provided or already set key/hashmap
def decode_function(hash_data: str) -> str:
    # default key
    key = "a_b?c9d6e1f4g!h:i<j|k{l0m@n7o+p~q2r+s/t=u^v3w]x(y-z>A*B8C;D%E#F}G5H)I[J$"
    # here we are creating a dictionary with with every even character as a key and every uneven character as a value
    chardict = dict(zip(key[1::2], key[::2]))
    decoded_string = ""
    # change the hash_data to uppercase
    hash_data = hash_data.upper()
    # loop through the hash_data and check if the character is in the dictionary,
    # if it is, add the value to the decoded_string
    for char in hash_data:
        if char in chardict:
            decoded_string += chardict[char]
    # add the decoded_string to the decoded_values list
    decoded_values.append(decoded_string)
    # return the decoded_string
    return decoded_string


# a function that encodes a string
def encode_string(hash_data: str, encode_function) -> str:
    return encode_function(hash_data)


# create a function that given the input string converts it to the
# decoded equivalent based on the provided or already set key/hashmap
# make sure to only decode values that are in the key, if the value is not present, use its own value
def decode_string(hash_data: str, decode_function) -> str:
    return decode_function(hash_data)


# create a function that given a list of inputs converts
# the complete list to the encoded equivalent based on the key/hashmap
# you can use the already created encode function when looping through the list
# tip! make use of the map function within python with a lambda to call the internal function with all elements
# as a return value, you should return a list with the converted values
def encode_list(hash_data: list, encode_function) -> list:
    encoded_string_list = []
    # loop through the hash_data and add the encoded string to the encoded_string_list
    for hash_data_item in hash_data:
        # here we are using a lambda function to call the encode_string function with the hash_data_item as a parameter
        encoded_string_list.append(lambda x: encode_string(hash_data_item, encode_function))
    # print the encoded_string_list
    print(encoded_string_list)
    # return the encoded_string_list
    return encoded_string_list


# create a function that given a list of inputs converts the complete list
# to the encoded equivalent based on the key/hashmap
# you can use the already created decode function when looping through the list
# tip! make use of the map function within python with a lambda to call the internal function with all elements
# as a return value, you should return a list with the converted values
def decode_list(hash_data: list, decode_function) -> list:
    # create a list to store the decoded strings
    decoded_string_list = []
    # loop through the hash_data and add the decoded string to the decoded_string_list
    for hash_data_item in hash_data:
        decoded_string_list.append(lambda x: decode_string(hash_data_item, decode_function))
    # print the decoded_string_list
    print(decoded_string_list)
    # return the decoded_string_list
    return decoded_string_list


# create a function that given a encoded value, decoded value and a key (optional) checks if the values are correct
# the return value should be a boolean value (True if values match, False if they don't match)
def validate_values(encoded: str, decoded: str, encode_function) -> bool:
    # check if the encoded value is the same as the encoded value of the decoded value
    if encode_string(decoded, encode_function) == encoded:
        return True
    else:
        return False


# give the option to input a hashvalue to be used/converted to a key
# each oneven character is the Key of the Dict, each even character is the coresponding Value
# you should validate if the given input is an even input, otherwise show the error: Invalid hashvalue input
# example: a@b.c>d#eA will become: {'a': '@', 'b': '.', 'c': '>', 'd', '#', 'e': 'A'}
def set_dict_key(key: str) -> None:
    # check if the key is even
    if len(key) % 2 != 0:
        print("Invalid hashvalue input")
        return
    # here we are creating a dictionary with with every uneven character as a key and every even character as a value
    chardict = dict(zip(key[1::2], key[::2]))
    print(chardict)
    # return the chardict
    return chardict


# build menu structure as following
# the input can be case-insensitive (so E and e are valid inputs)
# [E] Encode value to hashed value
# [D] Decode hashed value to normal value
# [P] Print all encoded/decoded values
# [V] Validate 2 values against eachother
# [Q] Quit program
def main():
    # create a while loop that will run until the user quits the program
    while True:
        # ask the user for a hashvalue to be used as a key
        hash_input = input("hash:")
        # print the menu
        print("""[E] Encode value to hashed value
[D] Decode hashed value to normal value
[P] Print all encoded/decoded values
[V] Validate 2 values against eachother
[Q] Quit program""")
        # check if the hash_input is the default hash_input
        if hash_input == "a_b?c9d6e1f4g!h:i<j|k{l0m@n7o+p~":
            pass
        # check if the hash_input is not long enough. The length should be 52
        elif len(hash_input) != 52:
            print("Invalid hashvalue input")
            break

        # ask the user for an action
        actie = input("Wat wilt u doen?")

        # check action, perform action based on input
        if actie.upper() == "E":
            keyinput = input("hash:")
            encode_string(keyinput, encode_function)

        elif actie.upper() == "D":
            keyinput = input("hash:")
            decode_string(keyinput, decode_function)

        elif actie.upper() == "P":
            printallvalues()
        elif actie.upper() == "V":
            encoded_hash_data = input("hash:")
            decoded_hash_data = input("hash:")
            validate_values(encoded_hash_data, decoded_hash_data,  encode_function)
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
# run main function
if __name__ == "__main__":
    main()