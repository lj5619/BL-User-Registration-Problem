import re

def validate_first_name(input_string):
    """
        Description:
            Funtion to check if the first name entered is valid or not
        Parameters:
            input string
        Return:
            None
    """
    pattern = r'^[A-Z][a-z]{2,}$'
    if re.fullmatch(pattern,input_string):
        print('Valid First Name')
    else:
        print('Invalid First Name')

def validate_last_name(input_string):
    """
        Description:
            Funtion to check if the last name entered is valid or not
        Parameters:
            input string
        Return:
            None
    """
    pattern = r'^[A-Z][a-z]{2,}$'
    if re.fullmatch(pattern,input_string):
        print('Valid Last Name')
    else:
        print('Invalid Last Name')

def main():

    first_name = input('Enter First Name: ')
    last_name = input('Enter Last Name: ')
    validate_first_name(first_name) 
    validate_last_name(last_name)
  

if __name__ == "__main__":
    main()

