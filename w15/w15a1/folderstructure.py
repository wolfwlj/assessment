# In a program a function is implemented to tranverse the folders and files.
# It returns the result as a list. A list indicates a folder and an string item is a file.

# For example: ['file_1',[]] is a folder that contains a file and an
# empty subfolder; ['file_1','file_2',['file_1']] is a folder containing two files and a subfolder with a file.
# Your task is to implement a Python function that:

# Given such a list as the root folder prints the contents.
# Indentation of the folder will be > and for a file will be -.
# Given such a list as the root folder prints the number of files.
# Im adding comments to this file to make it more readable.


# This function prints the contents of a given root folder with indentations.
def rec_print_folders(n: int, pref: str, root: list) -> None:
    '''  
    This function prints the contents of a given root folder with indentations.
    '''
    # set the indentation for the folder and file
    temp_folder_pref = ">" * n
    temp_file_pref = "-" * n
    # print the contents of the root folder
    print(f"{temp_folder_pref}Folder_{n}")
    # print the contents of the root folder
    for item in root:
        # if the item is a string, it is a file
        if type(item) == str:
            print(f"{temp_file_pref} {item}")
        # if the item is a list, it is a folder
        elif type(item) == list:
            # increase the indentation
            n += 1
            # call the function recursively
            rec_print_folders(n, pref, item)
            # decrease the indentation
            n -= 1
        # if the item is not a string or a list, it is an invalid type
        else:
            print("Invalid type")

    return None


# This function returns the number of files in a given root folder.
def rec_count_files(root: list) -> int:
    count = 0
    # iterate through the root folder
    for item in root:
        # if the item is a list, call the function recursively
        # if the item is a string, increase the count by 1
        if type(item) == str:
            count += 1
        elif type(item) == list:
            count += rec_count_files(item)

    return count


#  This block is for testing the functions.
if __name__ == "__main__":

    test_cases =[
        ['file_1',[]] ,
        ['file_1','file_2',['file_1']] ,
        ['file_1','file_2',['file_3','file_4','file_5'],['file_6',['file_7','file_8'],['file_9'],'file_9',['file_10']],[]] ,
        ['file_1',['file_3',['file_2',['file_10',['file_9','file_8']]]],[] ],
        [[],[[],[[]]]] 
        ]
    for case in test_cases:
        rec_print_folders(0,'',case)
        print('Number of files in case: ',case, ' is ',rec_count_files(case))