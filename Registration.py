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
        print('Invalid First Name \n First Name should start with capital letter')
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
        print('Invalid Last Name \n Last Name should start with capital letter')
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

    pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%+&*-]).{8,}$'
    if re.fullmatch(pattern,password):
        return True
    else:
        print('Invalid Password')
        return False

def main():

    while not validate_first_name(first_name := input('First Name: ')): pass
    while not validate_last_name(last_name := input('Last Name: ')): pass
    while not validate_email(email := input('Email ID: ')): pass
    while not validate_mobile(mobile_number := input('Enter mobile number with country code (Eg: 91 9812345123):' )): pass
    while not check_password(password := input('Enter Password (minimum 8 characters): ')): pass
    
    print (f'------------------------------ Welcome {first_name}------------------------------------')
    print(f'Full Name : {first_name} {last_name}')
    print(f'Email ID: {email}')
    print(f'Mobile Number: +{mobile_number}')

if __name__ == "__main__":
    main()
