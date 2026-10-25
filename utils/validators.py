def validate_person(first_name, last_name):
    first_name = first_name.strip()
    last_name = last_name.strip()
    if not first_name or not last_name:
        return False, "Please enter both first and last name."
    if len(first_name) > 40 or len(last_name) > 40:
        return False, "Names must be 40 characters or less."
    if not all(ch.isalpha() or ch in " -'" for ch in first_name + last_name):
        return False, "Names contain invalid characters."
    return True, ""

def validate_amount(value):
    try:
        amount = float(value)
    except (ValueError, TypeError):
        return False, 0, "Enter a valid amount."
    if amount <= 0:
        return False, 0, "Amount must be greater than zero."
    if amount > 1_000_000_000_000:
        return False, 0, "Amount is too large."
    return True, amount, ""
