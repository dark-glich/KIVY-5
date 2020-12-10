from validate_email import validate_email

def check(email):
    is_valid = validate_email(email_address=email, check_regex=True, check_mx=True)
    return is_valid


