import re
import logging


logging.basicConfig(filename='logs.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def validate_first_name(input_string):
    """
        Description:
            Function to check if the first name entered is valid or not
        Parameters:
            input_string
        Return:
            Boolean Value
    """
    pattern = r'^[A-Z][a-z]{2,}$'
    if re.fullmatch(pattern, input_string):
        logging.info("Valid first name entered.")
        return True
    else:
        error_message = 'Invalid First Name: First Name should start with a capital letter and have at least 3 characters.'
        print(error_message)
        logging.warning(error_message)
        return False

def validate_last_name(input_string):
    """
        Description:
            Function to check if the last name entered is valid or not
        Parameters:
            input_string
        Return:
            Boolean Value
    """
    pattern = r'^[A-Z][a-z]{2,}$'
    if re.fullmatch(pattern, input_string):
        logging.info("Valid last name entered.")
        return True
    else:
        error_message = 'Invalid Last Name: Last Name should start with a capital letter and have at least 3 characters.'
        print(error_message)
        logging.warning(error_message)
        return False

def validate_email(email):
    """
        Description:
            Function to check if the email entered is valid or not
        Parameters:
            email : email address in string
        Return:
            Boolean Value
    """
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z.]+\.[A-Za-z]{2,}$'
    if re.fullmatch(pattern, email):
        logging.info("Valid email address entered.")
        return True
    else:
        error_message = 'Invalid email address entered.'
        print(error_message)
        logging.warning(error_message)
        return False

def validate_mobile(mobile_number):
    """
        Description:
            Function to check if the mobile number entered is valid or not
        Parameters:
            mobile_number : mobile number in string
        Return:
            Boolean Value
    """
    pattern = r'^[0-9]{2,} [0-9]{10}$'
    if re.fullmatch(pattern, mobile_number):
        logging.info("Valid mobile number entered.")
        return True
    else:
        error_message = 'Invalid mobile number entered. Format should be like (e.g 91 9812345123)'
        print(error_message)
        logging.warning(error_message)
        return False

def check_password(password):
    """
        Description:
            Function to check if the password matches the rules
        Parameters:
            password
        Return:
            Boolean value
    """
    pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%+&*-]).{8,}$'
    special_chars = "!@#$%+&*-"
    count = sum(1 for char in password if char in special_chars)
    if re.fullmatch(pattern, password) and count == 1:
        logging.info("Valid password entered.")
        return True
    else:
        error_message = 'Invalid Password: Must have at least 8 characters, one uppercase letter, one digit, and one special character.'
        print(error_message)
        logging.warning(error_message)
        return False

def main():
    logging.info("User registration process started.")

    while not validate_first_name(first_name := input('First Name: ')): pass
    while not validate_last_name(last_name := input('Last Name: ')): pass
    while not validate_email(email := input('Email ID: ')): pass
    while not validate_mobile(mobile_number := input('Enter mobile number with country code (Eg: 91 9812345123): ')): pass
    while not check_password(password := input('Enter Password (minimum 8 characters): ')): pass

    logging.info("User registration completed successfully.")
    print(f'------------------------------ Welcome {first_name} ------------------------------------')
    print(f'Full Name : {first_name} {last_name}')
    print(f'Email ID: {email}')
    print(f'Mobile Number: +{mobile_number}')


if __name__ == "__main__":
    main()
