import re

def validate_first_name(input_string):
    """
        Description:
            Funtion to check if the first name entered is valid or not
        Parameters:
            input string
        Return:
            Boolean Value
    """
    pattern = r'^[A-Z][a-z]{2,}$'
    if re.fullmatch(pattern,input_string):
        return True
    else:
        print('Invalid First Name')
        return False

def validate_last_name(input_string):
    """
        Description:
            Funtion to check if the last name entered is valid or not
        Parameters:
            input string
        Return:
            Boolean Value
    """
    pattern = r'^[A-Z][a-z]{2,}$'
    if re.fullmatch(pattern,input_string):
        return True
    else:
        print('Invalid Last Name')
        return False
def validate_email(email):
    """
        Description:
            Funtion to check if the email entered is valid or not
        Parameters:
            email
        Return:
            Boolean Value
    """

    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z.]+\.[A-Za-z]{2,}$'
    if re.fullmatch(pattern,email):
        return True
    else:
        print('Invalid email address')
        return False

def validate_mobile(mobile_number):
    """
        Description:
            Funtion to check if the mobile number entered is valid or not
        Parameters:
            mobile number
        Return:
            Boolean Value
    """

    pattern = r'^[0-9]{2,} [0-9]{10}$'
    if re.fullmatch(pattern,mobile_number):
        return True
    else:
        print('Invalid mobile number')
        return False
    
def check_password(password):
    """
        Description:
            Funtion to check if the password matches the rules
        Parameters:
            password
        Return:
            Boolean value
    """

    pattern = r'^(?=.*[A-Z])(?=.*\d).{8,}$'
    if re.fullmatch(pattern,password):
        print('Password is Valid')
        return True
    else:
        print('Invalid Password')
        return False

def main():

    first_name = input('Enter First Name: ')
    last_name = input('Enter Last Name: ')
    email = input('Enter Email address: ')
    mobile_number = input('Enter mobile number with country code (Eg: 91 9812345123): ')
    password = input('Enter Password (minimum 8 characters): ')
    if validate_first_name(first_name) and validate_last_name(last_name) and validate_email(email) and validate_mobile(mobile_number) and check_password(password):
        print(f'Full Name is : {first_name} {last_name}')
        print(f'Email ID: {email}')
        print(f'Mobile Number: +{mobile_number}')
  
if __name__ == "__main__":
    main()

