has_high_income = True
has_good_credit = True
has_criminal_record = True

# AND -- both conditions must be True, else False
# OR -- at least one condition must be True, else False
# NOT -- Inverts a boolean value (ie. True becomes False and vice versa)

if has_high_income and has_good_credit:
    print('Eligible for loan!')

if has_high_income or has_good_credit:
    print('Eligible for loan!')

if has_good_credit and not has_criminal_record:
    print('Eligible for loan!')