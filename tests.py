import pytest

from Registration import (
    validate_first_name, 
    validate_last_name, 
    validate_email, 
    validate_mobile, 
    check_password
)

def test_validate_first_name():
    assert validate_first_name("Leon") == True
    assert validate_first_name("leon") == False 
    assert validate_first_name("6655@") == False 

def test_validate_last_name():
    assert validate_last_name("Olaprath") == True
    assert validate_last_name("olaprath") == False 
    assert validate_last_name("ola123") == False
def test_validate_email():
    assert validate_email("leon@gmail.com") == True
    assert validate_email("leon@gmail") == False 
    assert validate_email("leongmail.com") == False

def test_validate_mobile():
    assert validate_mobile("91 9987654321") == True
    assert validate_mobile("1234567890") == False 

def test_check_password():
    assert check_password("Leon%123") == True
    assert check_password("leon1222") == False
    assert check_password("leon@sss") == False