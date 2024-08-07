def check_pwd(str):

    symbols = '~`!@#$%^&*()_+-='

    # return false is length is 7 or less since length is 8 - 20
    if (len(str) <= 7 or len(str) >= 21):

        return False

    # Check if it has a lowercase digit
    has_lower = False
    for char in str:
        if char.islower():
            has_lower = True
            break

    if not has_lower:
        return False

    # Check for at least one uppercase letter
    has_upper = False
    for char in str:
        if char.isupper():
            has_upper = True
            break

    if not has_upper:
        return False

    # Checking if string has digits and does not have any digits at all
    has_digit = False
    for char in str:
        if char.isdigit():
            has_digit = True
            break

    if not has_digit:
        return False

    # Checking if the string has any symbols
    has_symbol = False
    for char in str:
        if char in symbols:
            has_symbol = True
            break

    # have to double check passwords that dont have one at all without returning true before
    if not has_symbol:
        return False

    return True
