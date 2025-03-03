import re

def validate_name(input_string):
    """
        Description:
            Funtion to check if the name entered is valid or not
        Parameters:
            input string
        Return:
            None
    """
    pattern = r'^[A-Z][a-z]{2,}$'
    if re.fullmatch(pattern,input_string):
        print('First Name is valid')
    else:
        print('First Name is invalid')

def main():

    input_string = input('Enter First Name: ')
    validate_name(input_string)


if __name__ == "__main__":
    main()

