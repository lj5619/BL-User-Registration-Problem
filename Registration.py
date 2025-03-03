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

def validate_email(email):
    """
        Description:
            Funtion to check if the email entered is valid or not
        Parameters:
            email
        Return:
            None
    """

    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z.]+\.[A-Za-z]{2,}$'
    if re.fullmatch(pattern,email):
        print('Valid email address')
    else:
        print('Invalid email address')

def validate_mobile(mobile_number):
    """
        Description:
            Funtion to check if the mobile number entered is valid or not
        Parameters:
            mobile number
        Return:
            None
    """

    pattern = r'^[0-9]{2,} [0-9]{10}$'
    if re.fullmatch(pattern,mobile_number):
        print('Valid mobile number')
    else:
        print('Invalid mobile number')

def main():

    first_name = input('Enter First Name: ')
    last_name = input('Enter Last Name: ')
    email = input('Enter Email address: ')
    mobile_number = input('Enter mobile number with country code (Eg: 91 9812345123): ')
    validate_first_name(first_name) 
    validate_last_name(last_name)
    validate_email(email)
    validate_mobile(mobile_number)
  

if __name__ == "__main__":
    main()

