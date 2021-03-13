# IDLE (Python 3.8.0)

# Round-Trip Time and Fraction Of Round-Trip Time

c = 299792458.0

def user_input_handling_function_sixth():
    print()
    user_input = input('Enter: ')
    print()
    good_to_go = 'no'
    errors = []
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
    while good_to_go == 'no':
        for_loop_broken = 'yes'
        while for_loop_broken == 'yes':
            for i in user_input:
                if i not in digits:
                    for_loop_broken = 'yes'
                    print('The number must consist of digits. For example: 1, 12, 123.1 or 1234.1')
                    print()
                    user_input = input('Re-enter: ')
                    print()
                    break
                else:
                    for_loop_broken = 'no'
        if float(user_input) <= 0:
            print('The velocity can\'t be less than or equal to 0 m/s.')
            errors.append('yes')
        if float(user_input) > 38_573_389.830_824_5:
            print('The velocity can\'t be greater than 38,573,389.830 824 5 m/s.')
            errors.append('yes')
        if 'yes' in errors:
            print()
            user_input = input('Re-enter: ')
            print()
            good_to_go = 'no'
            errors = []
            for_loop_broken = 'yes'
        else:
            good_to_go = 'yes'
    return float(user_input)

#####################################################################################################################################

print('The velocity of the ship is in m/s.')
print()
print('What is the velocity?') 
print()
V = user_input_handling_function_sixth()
# V means Velocity.
DAHT = c / 2.0 - (V / 2.0)
# DAHT means Distance After Half Time.
DAFT = DAHT - (DAHT / (c / V + 1.0))
# DAFT means Distance After Full Time.
TTTDAFTAc = DAFT / c
# TTTDAFTAc means Time To Travel DAFT At c.
RTT = TTTDAFTAc + 0.5
# RTT means Round-Trip Time.
FORTT = TTTDAFTAc / RTT
# FORTT means Fraction Of Round-Trip Time.
print('RTT:', RTT, 's')
print()
print('FORTT:', FORTT)
print()
