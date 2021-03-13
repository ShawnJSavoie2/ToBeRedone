# IDLE (Python 3.8.0)

# Number Of Worms, Length Of HP Each Worm Needs To Create, Length Of Each Worm and Diameter Of Each Worm

import math

# Possible Constants Related To Worms
MinLOHP = # ly 
# MinLOHP means Minimum Length Of Hyperspace Pathway.
MaxLOHP = # ly
# MaxLOHP means Maximum Length Of HP.
MSDBITOHP = 0.0001369863 # ly
# MSDBITOHP means Minimum Safe Distance Between Intermediate Terminals Of HPs. Note: 0.0001369863 ly is 0.5 days of travel at 0.1 c.
# It's 1 295 103 418.56 km. 
MinLOW = # km
# MinLOW means Minimum Length Of Worm.
MinDOW = # km
# MinDOW means Minimum Diameter Of Worm.
MaxDOW = # km
# MaxDOW means Maximum Diameter Of Worm.
TOH = # km
# TOH means Thickness Of Hull.
DOCC = # km
# DOCC means Diameter Of Conduit Coil.
DOHP = # km
# DOHP means Diameter Of HP.
HC = (TOH + DOCC) * 2
MMF = MaxDOW / MinDOW
# MMF means Maximum Multiplication Factor for diameter of worm.
MaxLOHPCWWOVD = ((MaxDOW + (HC * MMF - HC)) / MinDOW) ** 2 * MinLOHP
# MaxLOHPCWWOVD means Maximum Length Of HP Created With Worm Of Variable Diameter.

def user_input_handling_function_fifth():
    print()
    user_input = input('Enter: ')
    print()
    good_to_go = 'no'
    errors = []
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
    while good_to_go == 'no':
        for i in user_input:
            if i not in digits:
                print('The number must consist of digits. For example: 1, 12, 123.1 or 1234.1.')
                errors.append('yes')
                break
        if 'yes' in errors:
            print()
            user_input = input('Re-enter: ')
            print()
            good_to_go = 'no'
            errors = []
        else:
            good_to_go = 'yes'
    return user_input


print('The length of a HP is in Light Years (LY).')
print()
print('What is the length of the HP?') 
print()
LOHP = user_input_handling_function_fifth()
# LOHP means Length Of HP.
if LOHP < MinLOHP:
    print('NOW:', 0)
    # NOW means Number Of Worms.
else:
    NOW = LOHP / MaxLOHP
    if (NOW).is_integer() == True:
        LOHPEWNTC = (LOHP - ((NOW - 1.0) * MSDBITOHP)) / NOW
        # LOHPEWNTC means Length Of HP Each Worm Needs To Create.
        print('NOW:', NOW)
        print()
        print('LOHPEWNTC:', LOHPEWNTC, 'LY')
        print()
    else:
        NOW = math.ceil(NOW)
        LOHPEWNTC = (LOHP - ((NOW - 1.0) * MSDBITOHP)) / NOW
        print('NOW:', NOW)
        print()
        print('LOHPEWNTC:', LOHPEWNTC, 'LY')
        print()
    if LOHPEWNTC > MaxLOHPCWWOVD:
        LOEW = MinLOW * (LOHPEWNTC / MinLOHP)
        DOEW = MaxDOW
        print('LOEW:', LOEW, 'Km')
        print()
        print('DOEW:', DOEW, 'Km')
        print()
    else:
        LOEW = MinLOW * (LOHPEWNTC / MinLOHP)
        MF = math.sqrt(LOHPEWNTC / MinLOHP)
        ## MF means Multiplication Factor.
        DOEW = MinDOW * MF - (HC * MF - HC)
        print('LOEW:', LOEW, 'Km')
        print()
        print('DOEW:', DOEW, 'Km')
        print()

    #FOc = 0.125 #<<---- 
    # FOc means Fraction Of c. The sub-light velocity that the ship uses between intermediate terminals. 0.125 should be used to cut
    # down some time while still having adequate sensor capability. Unhashtag to test.

    #TTTHP = NOW * LOHPEWNTC / 64.0 + ((NOW - 1.0) * MSDBITOHP / FOc)
    ## TTTHP means Time To Travel HP. Unhashtag to test.
    #print("TTTHP:", TTTHP, "years,", TTTHP * 12, "months,", TTTHP * 365, "days")
    ## Unhashtag to test.
    #print((NOW - 1.0) * MSDBITOHP / FOc * 365, "days to travel distance between all intermediate terminals of the HPs")
    ## Unhashtag to test.
    #print((NOW - 1.0) * MSDBITOHP / FOc * 365 * 24, "hours to travel distance between all intermediate terminals of the HPs")
    ## Unhashtag to test.
