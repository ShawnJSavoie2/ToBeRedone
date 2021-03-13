# IDLE (Python 3.8.0)

# Time To Deceleration

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

print('The velocity of the ship is measured in meters/second.')
print()
print('What is the velocity of the ship?')
print()
V = user_input_handling_function_sixth()
# V means Velocity.
print('The time to process sensor data, initiate deceleration then decelerate is measured in seconds and it has to be equal to the')
print('time used in the MAV and DBSAD programs.')
print()
print('What is the time?')
T = user_input_handling_function_sixth()
# T means Time.
print('The distance between ships after deceleration is measured in meters.')
print()
print('What is the distance?')
DBSAD = user_input_handling_function_sixth()
# DBSAD means Distance Between Ships After Deceleration.
print('The reflection time is measured in seconds and it has to be equal to or less than the Round-Trip Time (RTT).')
print()
print('What is the time?')
RT = user_input_handling_function_sixth()
# RT means Reflection Time.

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
TTO = RT * FORTT
# TTO means Time To Object.
DTO = TTO * c
# DTO means Distance To Object.
HDTO = DTO / 2.0
# HDTO means Half DTO.
if HDTO <= V * (T - 0.5) + DBSAD: 
    print ('DECELERATE NOW!!!!')
else:
    TTD = (HDTO - (V * (T - 0.5) + DBSAD)) / V 
    # TTD means Time To Deceleration.
    print ('TTD:', TTD, 's (', TTD / 3600, 'hours,', TTD / 86400, 'days,', TTD
      / 31536000, 'years )')

    #print ("Test: HDTO - ((TTD * V) + (V * (T - 0.5))):", HDTO - ((TTD * V)
      #+ (V * (T - 0.5))), "m")
