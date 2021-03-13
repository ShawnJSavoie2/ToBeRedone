# IDLE (Python 3.8.0)

# Schedule For The Times To Accelerate A Hyperspace Pathway In 1-c Intervals Up To 64 c And The Time To Create A Hyperspace Pathway

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

print('The length of a HP is in light years (LY).')
print()
print('What is the length of the HP?')
print()
LOHP = user_input_handling_function_sixth()
# LOHP means Length Of HP.
HLOHP = LOHP / 2.0
# HLOHP means Half LOHP.
TBDEP = 0.00011415525 #years (3 600 seconds or 1 hour)
# TBDEP means Time Between Dissipating Energy Pulses.
WTBDEP = TBDEP
# WTBEP means Working TBDEP.
print ()
print ('After HP has been accelerated to 1 c accelerate it to:')
print ()
for MOc in range (2, 65):
# MOc means Multiple Of c.
    TTA = HLOHP / MOc * (MOc - 1.0) + WTBDEP
    # TTA means Time To Accelerate.
    WTBDEP = TBDEP * MOc
    print (MOc, 'c in', TTA, 'years,', TTA * 365, 'days,', TTA * 8760, 'hours')
TTCHP = HLOHP + (TBDEP * 64)
# TTCHP means Time To Create HP.
print ()
print ('TTCHP:', TTCHP, 'years,', TTCHP * 365, 'days')

# Note: A TBDEP is used because without one I fink that all the separate
# energy pulses should converge at once at the area where the HP is diverging
# and dissipating and where the exit will be and so the energy pulses should
# be 64 times more powerful than a single energy pulse and could be dangerous. 1
# hour was chosen because that gives --I fink-- sufficient time for each energy
# pulse to dissipate before the next one and without adding too much time to the
# creation process of a HP....
