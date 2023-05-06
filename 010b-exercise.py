price = 1_000_000
has_good_credit = False

if has_good_credit:
    down_payment = price * 0.10
    print(f'Down Payment: ${down_payment}')
else:
    down_payment = price * 0.20
    print(f'Down Payment: ${down_payment}')